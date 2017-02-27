import maestro
from Constants import *


class ArmControl:
    armChannelDict = {
        CONST_BASE_CHANNEL : [CONST_BASE_ANGLE_START, CONST_BASE_MIN_PWM, CONST_BASE_MAX_PWM,
                              CONST_BASE_MAX_ANGLE, CONST_BASE_SPEED, CONST_BASE_OFFSET],
        CONST_JOINT_1_CHANNEL : [CONST_JOINT_1_ANGLE_START, CONST_JOINT_1_MIN_PWM, CONST_JOINT_1_MAX_PWM,
                                 CONST_JOINT_1_MAX_ANGLE, CONST_JOINT_1_SPEED, CONST_JOINT_1_OFFSET],
        CONST_JOINT_2_CHANNEL : [CONST_JOINT_2_ANGLE_START, CONST_JOINT_2_MIN_PWM, CONST_JOINT_2_MAX_PWM,
                                 CONST_JOINT_2_MAX_ANGLE, CONST_JOINT_2_SPEED, CONST_JOINT_2_OFFSET],
        CONST_JOINT_3_CHANNEL : [CONST_JOINT_3_ANGLE_START, CONST_JOINT_3_MIN_PWM, CONST_JOINT_3_MAX_PWM,
                                 CONST_JOINT_3_MAX_ANGLE, CONST_JOINT_3_SPEED, CONST_JOINT_3_OFFSET],
        CONST_GRIPPER_CHANNEL : [CONST_GRIPPER_ANGLE_START, CONST_GRIPPER_MIN_PWM, CONST_GRIPPER_MAX_PWM,
                                 CONST_GRIPPER_MAX_ANGLE, CONST_GRIPPER_SPEED, CONST_GRIPPER_OFFSET]
    }

    def __init__(self):
        self.joint = maestro.Controller()
        self.joint.setRange(CONST_BASE_CHANNEL, CONST_BASE_MIN_PWM, CONST_BASE_MAX_PWM)
        self.joint.setRange(CONST_JOINT_1_CHANNEL, CONST_JOINT_1_MIN_PWM, CONST_JOINT_1_MAX_PWM)
        self.joint.setRange(CONST_JOINT_2_CHANNEL, CONST_JOINT_2_MIN_PWM, CONST_JOINT_2_MAX_PWM)
        self.joint.setRange(CONST_JOINT_3_CHANNEL, CONST_JOINT_3_MIN_PWM, CONST_JOINT_3_MAX_PWM)
        self.joint.setRange(CONST_GRIPPER_CHANNEL, CONST_GRIPPER_MIN_PWM, CONST_GRIPPER_MAX_PWM)


    def getCurrentAngle(self, channel):
        return self.joint.getPosition(channel)

    def setAngle(self, channel, angle):
        jointAnglePWM = angle * ((self.armChannelDict[channel][2] -
                                self.armChannelDict[channel][1]) /
                                self.armChannelDict[channel][3]) + \
                                self.armChannelDict[channel][1]
        self.joint.setTarget(channel, jointAnglePWM)
        self.joint.setAccel(channel, self.armChannelDict[channel][4])

    def close(self):
        self.joint.close()