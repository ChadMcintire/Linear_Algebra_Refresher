class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

        except IndexError:
            raise IndexError('The size of the arrays is not the same')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
                                                                               
    def __add__(self, v):
        if self.dimension != v.dimension:
            raise IndexError
        else:
            combined_array = [0 for _ in range(self.dimension)]
            for i in range(self.dimension):
                combined_array[i] = self.coordinates[i] + v.coordinates[i]    
            return Vector(combined_array)

    def __sub__(self, v):
        if self.dimension != v.dimension:
            raise IndexError
        else:
            combined_array = [0 for _ in range(self.dimension)]
            for i in range(self.dimension):
                combined_array[i] = self.coordinates[i] - v.coordinates[i]    
            return Vector(combined_array)

    def scalar(self, scalar_value):
        combined_array = [0 for _ in range(self.dimension)]
        for i in range(self.dimension):
            combined_array[i] = self.coordinates[i] * scalar_value
        return Vector(combined_array)

if __name__ == "__main__":
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])
    v3 = Vector([7.119, 8.215])
    v4 = Vector([-8.223, 0.878])
    v5 = Vector([1.671, -1.012, -0.318])
    print(v1 + v2)
    print(v3 - v4)
    print(v5.scalar(7.41))

