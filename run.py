# from UPISAS.strategies.swim_reactive_strategy import ReactiveAdaptationManager
# from UPISAS.exemplar import Exemplar
# from UPISAS.exemplars.swim import SWIM
# import signal
# import sys
# import time

# if __name__ == '__main__':
    
#     exemplar = SWIM(auto_start=True)
#     time.sleep(3)
#     exemplar.start_run()
#     time.sleep(3)

#     try:
#         strategy = ReactiveAdaptationManager(exemplar)

#         strategy.get_monitor_schema()
#         strategy.get_adaptation_options_schema()
#         strategy.get_execute_schema()

#         while True:
#             input("Try to adapt?")
#             strategy.monitor(verbose=True)
#             if strategy.analyze():
#                 if strategy.plan():
#                     strategy.execute()
            
#     except (Exception, KeyboardInterrupt) as e:
#         print(str(e))
#         input("something went wrong")
#         exemplar.stop_container()
#         sys.exit(0)

from UPISAS.strategies.demo_strategy import DemoStrategy
from UPISAS.exemplar import Exemplar
from UPISAS.exemplars.demo_exemplar import DemoExemplar
import signal
import sys
import time

if __name__ == '__main__':
    
    exemplar = DemoExemplar(auto_start=True)
    time.sleep(3)
    time.sleep(3)

    try:
        strategy = DemoStrategy(exemplar)

        strategy.get_monitor_schema()
        print(strategy.knowledge.monitor_schema)
        strategy.get_adaptation_options_schema()
        strategy.get_execute_schema()

        while True:
            input("Try to adapt?")
            strategy.monitor(verbose=True)
            # if strategy.analyze():
            #     if strategy.plan():
            #         strategy.execute()
            
    except (Exception, KeyboardInterrupt) as e:
        print(str(e))
        input("something went wrong")
        exemplar.stop_container()
        sys.exit(0)


