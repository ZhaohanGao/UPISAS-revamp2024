from UPISAS.exemplar import Exemplar


class DemoExemplar(Exemplar):
    """
    A class which encapsulates a self-adaptive exemplar run in a docker container.
    """
    def __init__(self, auto_start=False, container_name="api-server"):
        docker_config = {
            "name":  container_name,
            "image": "zhaohangao/api-service:latest",
            "ports" : {50000: 50000},
            "network": "ramses-sas-net"
            }
        super().__init__("http://localhost:50000", docker_config, auto_start)

    def start_run(self, app):
        self.exemplar_container.exec_run(cmd = f' sh -c "cd /usr/src/app && node {app}" ', detach=True)
