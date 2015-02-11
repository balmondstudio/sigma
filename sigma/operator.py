import math


class Operator:

    def __init__(self):
        pass

    def operate(self, dto):
        raise NotImplementedError


class DigitalRoot(Operator):

    def __init__(self):
        super().__init__()

    def _digital_root(self, n):
        return n - 9 * math.floor((n - 1) / 9)

    def operate(self, dto):
        for primitive in dto:
            primitive.value.data = self._digital_root(primitive.value.n)

        return dto


class Crystal(Operator):

    def __init__(self):
        super().__init__()

    def curves(self):
        curves = []
        for instruction in self._instructions:
            positions = self._mapper.getValue(instruction - 1)

        for start in positions:
            parameter = sigma.finder.FinderParameter(
                key = instruction - 1,
                position = start,
                direction = sigma.geometry.Vector([1, 1, 1]),
                space = [value for value in positions if value != start]
                )
            curve = self.curve(parameter)

            #curves.append(curve)
            curves.extend(curve)
        return curves

#def curve(self, parameter):
  #  curve = []
  #  for i in range(min(self._size, len(parameter.space))):
  #    curve.append(parameter.position)
  #    parameter.update(self._finder.search(parameter)[0])
  #    #parameters.update(self._finder.search(parameters)[-1])
  #  return curve

  def curve(self, parameter):
      tree = [[parameter.position]]

    for __ in range(min(self._size - 1, len(parameter.space))):
        for branch in list(tree):
            try:
                parameter = sigma.finder.FinderParameter(
                        key = parameter.key,
                        position = branch[-1],
                        direction = branch[-2] - branch[-1],
                        space = [value for value in parameter.space if value != branch[-1]])
        except IndexError:
            pass

        tree.remove(branch)
        for found in self._finder.search(parameter):
            tree.append(branch + [found])

    print tree[0]
    return tree

# def curve(self, tree):
  #   for __ in range(min(self._size, len(parameter.space))):
  #     for branch in list(tree):
  #       tree.remove(branch)
  #       tree.extend([branch + [found] for found in self._finder.search(branch[-1])])
  #   return tree

  # def curve(self, node):
  #   tree = []

  #   for __ in range(min(self._size, len(parameter.space))):
  #     for branch in list(tree):
  #       tree.remove(branch)
  #       tree.extend([branch + [found] for found in self._finder.search(branch[-1])])

  #     if not tree: tree.append([node])

  #   return tree
