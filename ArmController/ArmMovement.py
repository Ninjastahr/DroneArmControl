import maestro
from Constants import *


class ArmControl:
    armJointCurrAngle = [0, 0, 0, 0, 0]
    armJointMaxAngle = [0, 0, 0, 0, 0]
    armJointMinPWM = [0, 0, 0, 0, 0]
    armJointMaxPWM = [0, 0, 0, 0, 0]
    armJointSpeed = [0, 0, 0, 0, 0]

    def __init__(self):
        self.armJointCurrAngle[0] = CONST_BASE_ANGLE_START
        self.armJointCurrAngle[1] = CONST_JOINT_1_ANGLE_START
        self.armJointCurrAngle[2] = CONST_JOINT_2_ANGLE_START
        self.armJointCurrAngle[3] = CONST_JOINT_3_ANGLE_START
        self.armJointCurrAngle[4] = CONST_GRIPPER_ANGLE_START

        self.armJointMinPWM[0] = CONST_BASE_MIN_PWM
        self.armJointMinPWM[1] = CONST_JOINT_1_MIN_PWM
        self.armJointMinPWM[2] = CONST_JOINT_2_MIN_PWM
        self.armJointMinPWM[3] = CONST_JOINT_3_MIN_PWM
        self.armJointMinPWM[4] = CONST_GRIPPER_MIN_PWM

        self.armJointMaxPWM[0] = CONST_BASE_MAX_PWM
        self.armJointMaxPWM[1] = CONST_JOINT_1_MAX_PWM
        self.armJointMaxPWM[2] = CONST_JOINT_2_MAX_PWM
        self.armJointMaxPWM[3] = CONST_JOINT_3_MAX_PWM
        self.armJointMaxPWM[4] = CONST_GRIPPER_MAX_PWM

        self.armJointMaxAngle[0] = CONST_BASE_MAX_ANGLE
        self.armJointMaxAngle[1] = CONST_JOINT_1_MAX_ANGLE
        self.armJointMaxAngle[2] = CONST_JOINT_2_MAX_ANGLE
        self.armJointMaxAngle[3] = CONST_JOINT_3_MAX_ANGLE
        self.armJointMaxAngle[4] = CONST_GRIPPER_MAX_ANGLE

        self.armJointSpeed[0] = CONST_BASE_SPEED
        self.armJointSpeed[1] = CONST_JOINT_1_SPEED
        self.armJointSpeed[2] = CONST_JOINT_2_SPEED
        self.armJointSpeed[3] = CONST_JOINT_3_SPEED
        self.armJointSpeed[4] = CONST_GRIPPER_SPEED

        self.joint = maestro.Controller()
        self.joint.setRange(CONST_BASE_CHANNEL, CONST_BASE_MIN_PWM, CONST_BASE_MAX_PWM)
        self.joint.setRange(CONST_JOINT_1_CHANNEL, CONST_JOINT_1_MIN_PWM, CONST_JOINT_1_MAX_PWM)
        self.joint.setRange(CONST_JOINT_2_CHANNEL, CONST_JOINT_2_MIN_PWM, CONST_JOINT_2_MAX_PWM)
        self.joint.setRange(CONST_JOINT_3_CHANNEL, CONST_JOINT_3_MIN_PWM, CONST_JOINT_3_MAX_PWM)
        self.joint.setRange(CONST_GRIPPER_CHANNEL, CONST_GRIPPER_MIN_PWM, CONST_GRIPPER_MAX_PWM)


    def getCurrentAngle(self, channel):
        return self.armJointCurrAngle[channel]

    def setAngle(self, channel, angle):
        jointAnglePWM = angle * ((self.armJointMaxPWM[channel] - self.armJointMinPWM[channel]) /
                                 self.armJointMaxAngle[channel]) + self.armJointMinPWM[channel]
        self.joint.setTarget(channel, jointAnglePWM)
        self.joint.setAccel(channel, self.armJointSpeed[channel])
        self.armJointCurrAngle[channel] = angle

    def close(self):
        self.joint.close()