import os
import psutil
import lucy
class SystemHealthSkills:

    @classmethod
    def tell_memory_consumption(cls,_):
        """
        Responds the memory consumption of the assistant process.
        """
        memory = cls._get_memory_consumption()
        lucy.output_engine.respond("I use {0:.2f} GB..".format(memory))

    @classmethod
    def _get_memory_consumption(cls):
        pid = os.getpid()
        py = psutil.Process(pid)
        memory_use = py.memory_info()[0] / 2. ** 30  # memory use in GB...I think
        return memory_use
