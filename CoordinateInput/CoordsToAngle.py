from ArmController import ArmMovement
from Constants import *
import math

class ArmAngleCalculator:
    channels = [CONST_BASE_CHANNEL, CONST_JOINT_1_CHANNEL,
                CONST_JOINT_2_CHANNEL, CONST_JOINT_3_CHANNEL, CONST_GRIPPER_CHANNEL]

    def __init__(self):
        self.a1 = ARM_1_LENGTH
        self.a2 = ARM_2_LENGTH

        self.angle1 = 0
        self.angle1Alt = 0
        self.angle2 = 0
        self.angle3 = 0

        self.x = 0
        self.y = 0
        self.z = 0
        self.arm = ArmMovement.ArmControl()


    def calculateAngle(self):
        v = self.a1
        u = self.a2
        pX = self.x
        pY = self.y

        A = math.sqrt(pX * pX + pY * pY)
        B = self.z
        d = math.sqrt(A * A + B * B)

        aTemp1 = math.atan(B / A)
        aTemp2 = math.acos((u * u - (A * A + B * B) - v * v)/(-2 * math.sqrt(A * A + B * B) * v))

        temp2 = math.acos((pX * pX + pY * pY + B * B - v * v - u * u) / (-2 * v * u))
        temp3 = math.atan(pY / pX)
        alpha2 = math.acos((u * u - d * d - v * v) / (-2 * d * v))

        self.angle1 = math.degrees(aTemp1 - aTemp2)
        self.angle1Alt = 2 * math.degrees(alpha2) + self.angle1
        self.angle2 = 180 - math.degrees(temp2)
        self.angle3 = math.degrees(temp3)

    def setPoint(self, xIn, yIn, zIn):
        self.x = xIn
        self.y = yIn
        self.z = zIn
        self.calculateAngle()

    def moveArm(self):
        self.arm.setAngle(channels[0], self.angle3)
        self.arm.setAngle(channels[1], self.angle1)
        self.arm.setAngle(channels[2], self.angle2)
