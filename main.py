import MachineConfig
import PrintMenuDisplay
import Encoder
import StepperMotor

config = MachineConfig()
menu = PrintMenuDisplay(menu_items=[], descriptions=['Добро пожаловать', 'в NGF Controller'], values=[])
ecoder = Encoder(config.get_encoder_pins().clk, config.get_encoder_pins().dt)

motorX = StepperMotor(step_pin=config.get_stepper_pins('X').step, dir_pin=config.get_stepper_pins('X').dir, steps_per_mm=100, acceleration=0.1)
motorY = StepperMotor(step_pin=config.get_stepper_pins('Y').step, dir_pin=config.get_stepper_pins('Y').dir, steps_per_mm=100, acceleration=0.1)
motorZ = StepperMotor(step_pin=config.get_stepper_pins('Z').step, dir_pin=config.get_stepper_pins('Z').dir, steps_per_mm=100, acceleration=0.1)



while True:
    
    position = encoder.read()

    
