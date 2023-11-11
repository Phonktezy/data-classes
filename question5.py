#1
# from dataclasses import dataclass
# class AirCastle:
#     def __init__(self, h, c, cl):
#         self.h = h
#         self.c = c
#         self.cl = cl
#
# @dataclass
# class AirData:
#     h: int
#     c: int
#     cl: str
#
#
#     def c_c(self, value):
#         s = self.c + value
#         if s < 0:
#             c = 0
#         self.c
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError('error')
#         self.c += other
#         self.h += other // 5
#         print(self.h)
#         return AirData (self.h, self.c, self.cl)
#
#     def opacity(self, degree):
#         self.degree = self.h // degree * self.cl
#         print(f'Прозрачность облака: {self.degree}')
#
#     def __str__(self):
#         return f'The AirCastle at an altitude of {self.h} meters is {self.c} with {self.cl} clouds'
#
#     def __eq__(self, other):
#         if not isinstance(other, AirData):
#             raise TypeError
#         return self.cl == other.cl
#     def __lt__(self, other):
#         if not isinstance(other, AirData):
#             raise TypeError
#         return self.cl < other.cl
#     def __le__(self, other):
#         if not isinstance(other, AirData):
#             raise TypeError
#         return self.cl <= other.cl
#
#
# castle = AirData(120, 20, 'green')
# castle1 = AirData(120, 20, 'green')
# print(castle)
# castle.c_c(5)
# castle.c_c(-10)
# print(castle)
# castle = castle+10
# print(castle)
# castle.opacity(5)
# print(castle)
# print(castle == castle1)
# print(castle < castle1)
#2
# @dataclass
# class Kindness:
#     high: int
#     name: str
#     happy: int
#
#     def cg(self, mood):
#         x = self.happy + mood
#         if x < 0:
#             x = 0
#         self.happy = x
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError('ERROR')
#         return(Kindness(self.high + other, self.name, self.happy))
#
#     def arguments(self, param):
#         return f'{param * self.happy // self.high}'
#
#     def __str__(self):
#         return f' Good Ifrit {self.name}, height {self.high}. kindness {self.happy}'
#
#     def __eq__(self, other):
#         if not isinstance(other, Kindness):
#              raise TypeError ('error')
#         return (self.high, other.happy, self.name) == (other.happy, other.high, other.name)
#
#     def __gt__(self, other):
#         if not isinstance(other, Kindness):
#              raise TypeError ('error')
#         return (self.high, other.happy, self.name) > (other.happy, other.high, other.name)
#
#     def __len__(self, other):
#         if not isinstance(other, Kindness):
#              raise TypeError ('error')
#         return (self.high, other.happy, self.name) >= (other.happy, other.high, other.name)
#
# a = Kindness(10, 'Vasya', -2)
# a1 = Kindness(10, 'Vasya', -2)
# a.cg(52)
# print(a)
# print(a + 5)
# print(a.arguments(5))
# print(a > a1)


