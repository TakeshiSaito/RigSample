from RigSample.Character.IHip import IHip


class Hip(IHip):

    def __init__(self, namespace):
        self.__namespace = namespace

    @property
    def hip_joint(self):
        return f"{self.__namespace}:CC_Base_Hip"
