import json

def assignWeight():
        a = 0.7
        with open('data.json', 'r') as file:
            data = json.load(file)  # 将文件中的 JSON 数据解析为 Python 字典
        # data = self.knowledge.monitored_data
        # print(data)
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

dic = assignWeight()
print(dic)