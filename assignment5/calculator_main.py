from view import View
from controller import Controller
from calculator_model import CalculatorModel
from subject import Subject, Observer
if __name__ == '__main__':
    ''' Main function, instantiate instances of Model, View and a Controller'''

    model = CalculatorModel()
<<<<<<< HEAD
    view = View(model=model)
=======
    view = View()
    model.attach(view)
>>>>>>> 8c64d1c319c2e805cd0f21895f34bb214f5f6baa

    controller = Controller(model=model, view=view)
    controller.run()