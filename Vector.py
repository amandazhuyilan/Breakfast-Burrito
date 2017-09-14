class Vector:
#Represent a vector in a multi-dimentional space
    def __init__(self, d):
    #Creates a d-dimentional vector of zeros.
        self._coords = [0] * d

    def __len__(self):
    #returns the dimension of the vector 
        return len(self._coords)

    def __getitem__(self, j, val):
    #set jth coordinate to the given value
        self._coords[j] = val

    def __add__(self,other):
    #adding two vectors
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
    #return True if two vectors are equal
        if self._coords ==  other._coords:
            return True
        else:
            return False

    def __str__(self):
    #return string representation of vector
        return '<' + str(self._coords[1:-1]) + '>' #[1:-1] return all in list except the last 
