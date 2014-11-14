class ExampleClass(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (list of str): Description of `attr2`.
      attr3 (int): Description of `attr3`.

    """
    def __init__(self, param1, param2, param3=0):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1 (str): Description of `param1`.
          param2 (list of str): Description of `param2`. Multiple
            lines are supported.
          param3 (int, optional): Description of `param3`, defaults to 0.

        """
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = param3

    def example_method(self, param1, param2):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return True

    def __special__(self):
        """By default special members with docstrings are included.

        Special members are any methods or attributes that start with and
        end with a double underscore. Any special member with a docstring
        will be included in the output.

        This behavior can be disabled by changing the following setting in
        Sphinx's conf.py::

            napoleon_include_special_with_doc = False

        """
        pass

    def __special_without_docstring__(self):
        pass

    def _private(self):
        """By default private members are not included.

      Private members are any methods or attributes that start with an
      underscore and are *not* special. By default they are not included
      in the output.

      This behavior can be changed such that private members *are* included
      by changing the following setting in Sphinx's conf.py::

          napoleon_include_private_with_doc = True

      """
      pass

  def _private_without_docstring(self):
      pass
