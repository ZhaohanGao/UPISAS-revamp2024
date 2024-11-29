from UPISAS.strategy import Strategy

#This is a port of the ReactiveAdaptationManager originally published alongside SWIM.
class ReactiveAdaptationManager(Strategy):
    a = 0.7
    
    def assignWeight(self):
        data = self.knowledge.monitored_data
        print(data)
        # names if instances list
        instances_name = data["ORDERING-SERVICE"]["instances"] 
        print(instances_name)
        # get numbers of instances
        instances_numbers = len(instances_name)
        snapshots = data["ORDERING-SERVICE"]["snapshot"]

        cpuUsage_list = []
        RT_list = []
        for snapshot in snapshots:
            cpuUsage = float(snapshot["cpuUsage"]) * 1000
            cpuUsage_list.append(cpuUsage)
            # get each instance RT
            total_duration_sum = sum(
                endpoint_data["outcomeMetrics"]["SUCCESS"]["totalDuration"]
                for endpoint_data in snapshot["httpMetrics"].values()
            ) /1000
            RT_list.append(total_duration_sum)
        max_RT = max(RT_list)
        min_RT = min(RT_list)
        scores = []    
        weights = []
        for i in range(instances_numbers):
            NormRT = (RT_list[i] - min_RT)/(max_RT - min_RT)
            score = 1/ (a * cpuUsage_list[i] + (1 - a) *NormRT)
            scores.append(score)
        # get weight
        for i in range(instances_numbers):

            weight = scores[i] / sum(scores)
            weights.append(weight)
        # combine instance name and weight return the dic
        dict = {}
        for i in range(instances_numbers):
            dict[instances_name[i]] = weights[i]
        return dict




    def analyze(self):
        if("next_operation" not in knowledge.analysis_data 
            or knowledge.analysis_data["next_operation"] == "changeLBWeights"):
            knowledge.analysis_data["next_operation"] = "addInstances"
        else:    
            dic = assignWeight()        
            self.knowledge.analysis_data["instances_number"] = len(dic)
            self.knowledge.analysis_data["newWeights"] = dic
        return True
        

    def plan(self):
        if(self.knowledge.analysis_data["next_operation"] == "addInstances"):
            self.knowledge.plan_data["operation"] = "addInstances"
            self.knowledge.plan_data["serviceImplementationName"] = "ordering-service"
            self.knowledge.plan_data["numberOfInstances"] = 1
            knowledge.analysis_data.clear()
            knowledge.analysis_data["next_operation"] = "changeLBWeights"
        else:
            self.knowledge.plan_data["operation"] = knowledge.analysis_data["next_operation"]
            self.knowledge.plan_data["serviceId"] = "ORDERING-SERVICE"
            self.knowledge.plan_data["newWeights"] = self.knowledge.analysis_data["newWeights"]
            knowledge.analysis_data.clear()
            knowledge.analysis_data["next_operation"] = "addInstances"

        





        
        