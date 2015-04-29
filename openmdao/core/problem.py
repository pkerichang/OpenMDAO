""" Defines the base class for a component in"""

from openmdao.core.component import Component

class Problem(Component):
    def __init__(self, root=None, driver=None):
        self.root = root
        self.driver = driver

    def setup(self):
        pass

    def run(self):
        pass

    def calc_gradient(self, inputs=None, outputs=None, mode='auto',
                      return_format='array'):
        """ Returns the gradient for the system that is slotted in
        self.root. This function is used by the optimizer, but also can be
        used for testing derivatives on your model.

        inputs: list of strings (optional)
            List of parameter name strings with respect to which derivatives
            are desired. All params must have a paramcomp. Default is None,
            which uses all ParamSystems as inputs.

        outputs: list of strings (optional)
            List of output or state name strings for derivatives to be
            calculated. All must be valid outputs. Default is None, which
            calculate derivatives for all outputs with no corresponding
            connection targets.

        mode: string (optional)
            Deriviative direction, can be 'fwd', 'rev', or 'auto'.
            Default is 'auto', which uses mode specified on the linear solver
            in root.

        return_format: string (optional)
            Format for the derivatives, can be 'array' or 'dict'.
        """

        if mode not in ['auto', 'fwd', 'rev']:
            msg = "mode must be 'auto', 'fwd', or 'rev'"
            raise ValueError(msg)

        if return_format not in ['array', 'dict']:
            msg = "return_format must be 'array' or 'dict'"
            raise ValueError(msg)

        # Here, we will assemble right hand sides and call solve_linear on the
        # system in root for each of them.

        pass
