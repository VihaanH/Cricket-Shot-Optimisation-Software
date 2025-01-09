from sympy import symbols, sin, diff, solve, Eq, nsolve, pi, cos
from math import sqrt
import sys
a, g, theta  = 0.00743, 9.81, pi/4  # Integral K Value calculation
V0, Wind_Speed = symbols('V0, Wind_Speed')

Wankhede_dimensions = {"Cover Drive" : 72, "Upper Cut" : 58, "Cut" : 64, "Straight Drive" : 76, "Long on Lofted" : 76, "Pull" : 69, "Scoop" : 63}
User1 = float(sys.argv[1])
User2 = str(sys.argv[2])
k = 0.00475 * V0
v_wind_x = User1 * sqrt(2)/2
v_wind_y = User1 * sqrt(2)/2
result = []
if User2 == 'North to South' :
    for key in Wankhede_dimensions:
        if key == "Upper Cut" or key == "Scoop" :
            equation1 =  (
    (V0 * cos(theta) - v_wind_x) * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) - v_wind_x) * k * (2 * (V0 * sin(theta) - v_wind_y) / ((V0 * sin(theta) - v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g)
)
            if key == "Upper Cut":
                Dimension1 = Wankhede_dimensions.get("Upper Cut")
                Initial_Speed1 = nsolve(equation1 - Dimension1, V0, 10)
                result.append((Initial_Speed1, "Upper Cut"))
            if key == "Scoop":
                Dimension2 = Wankhede_dimensions.get("Scoop")
                Initial_Speed2 = nsolve(equation1 - Dimension2, V0, 10)
                result.append((Initial_Speed2, "Scoop"))
        if key == "Straight Drive" or key == "Long on Lofted":
            equation2 = (
    (V0 * cos(theta) + v_wind_x) * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) + v_wind_x) * k * (2 * (V0 * sin(theta) + v_wind_y) / ((V0 * sin(theta) + v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g)
            )
            if key == "Straight Drive":
                Dimension3 = Wankhede_dimensions.get("Straight Drive")
                Initial_Speed3 = nsolve(equation2 - Dimension3, V0, 10)
                result.append((Initial_Speed3, "Straight Drive"))
            if key == "Long on Lofted":
                Dimension4 = Wankhede_dimensions.get("Long on Lofted")
                Initial_Speed4 = nsolve(equation2 - Dimension4, V0, 10)
                result.append((Initial_Speed4, "Long on Lofted"))
        else:
            equation3 =  (
    (V0 * cos(theta) ) * (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g) 
    - 0.5 * (V0 * cos(theta) ) * k * (2 * (V0 * sin(theta) ) / ((V0 * sin(theta) ) * k + g))**2 
    +  (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g)
            )
            if key == "Cover Drive" :
                Dimension5 = Wankhede_dimensions.get("Cover Drive")
                Initial_Speed5 = nsolve(equation3 - Dimension5, V0, 10)
                result.append((Initial_Speed5, "Cover Drive"))
            if key == "Cut":
                Dimension6 = Wankhede_dimensions.get("Cut")
                Initial_Speed6 = nsolve(equation3 - Dimension6, V0, 10)
                result.append((Initial_Speed6, "Cut"))
            if key == "Pull":
                Dimension7 = Wankhede_dimensions.get("Pull")
                Initial_Speed7 = nsolve(equation3 - Dimension7, V0, 10)
                result.append((Initial_Speed7, "Pull"))

if User2 == 'South to North':
    for key in Wankhede_dimensions:
        if key == "Upper Cut" or key == "Scoop" :
            equation2 = (
    (V0 * cos(theta) + v_wind_x) * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) + v_wind_x) * k * (2 * (V0 * sin(theta) + v_wind_y) / ((V0 * sin(theta) + v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g)
            )
            if key == "Upper Cut":
                Dimension1 = Wankhede_dimensions.get("Upper Cut")
                Initial_Speed8 = nsolve(equation2 - Dimension1, V0, 10)
                result.append((Initial_Speed8, "Upper Cut"))
            if key == "Scoop":
                Dimension2 = Wankhede_dimensions.get("Scoop")
                Initial_Speed9 = nsolve(equation2 - Dimension2, V0, 10)
                result.append((Initial_Speed9, "Scoop"))
        if key == "Straight Drive" or key == "Long on Lofted":
            equation1 =  (
    (V0 * cos(theta) - v_wind_x) * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) - v_wind_x) * k * (2 * (V0 * sin(theta) - v_wind_y) / ((V0 * sin(theta) - v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g)
)
            if key == "Straight Drive":
                Dimension3 = Wankhede_dimensions.get("Straight Drive")
                Initial_Speed10 = nsolve(equation1 - Dimension3, V0, 10)
                result.append((Initial_Speed10, "Straight Drive"))
            if key == "Long on Lofted":
                Dimension4 = Wankhede_dimensions.get("Long on Lofted")
                Initial_Speed11 = nsolve(equation1 - Dimension4, V0, 10)
                result.append((Initial_Speed11, "Long on Lofted"))
        else:
            equation3 =  (
    (V0 * cos(theta) ) * (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g) 
    - 0.5 * (V0 * cos(theta) ) * k * (2 * (V0 * sin(theta) ) / ((V0 * sin(theta) ) * k + g))**2 
    +  (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g)
            )
            if key == "Cover Drive" :
                Dimension5 = Wankhede_dimensions.get("Cover Drive")
                Initial_Speed5 = nsolve(equation3 - Dimension5, V0, 10)
                result.append((Initial_Speed5, "Cover Drive"))
            if key == "Cut":
                Dimension6 = Wankhede_dimensions.get("Cut")
                Initial_Speed6 = nsolve(equation3 - Dimension6, V0, 10)
                result.append((Initial_Speed6, "Cut"))
            if key == "Pull":
                Dimension7 = Wankhede_dimensions.get("Pull")
                Initial_Speed7 = nsolve(equation3 - Dimension7, V0, 10)
                result.append((Initial_Speed7, "Pull"))

if User2 == 'East to West':
    for key in Wankhede_dimensions:
        if key == "Upper Cut" or key == "Scoop" or key == "Long on Lofted" or key == "Straight Drive":
            equation3 =  (
    (V0 * cos(theta) ) * (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g) 
    - 0.5 * (V0 * cos(theta) ) * k * (2 * (V0 * sin(theta) ) / ((V0 * sin(theta) ) * k + g))**2 
    +  (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g)
            )
            if key == "Straight Drive":
                Dimension3 = Wankhede_dimensions.get("Straight Drive")
                Initial_Speed12 = nsolve(equation3 - Dimension3, V0, 10)
                result.append((Initial_Speed12, "Straight Drive"))
            if key == "Long on Lofted":
                Dimension4 = Wankhede_dimensions.get("Long on Lofted")
                Initial_Speed13 = nsolve(equation3 - Dimension4, V0, 10)
                result.append((Initial_Speed13, "Long on Lofted"))
            if key == "Upper Cut":
                Dimension1 = Wankhede_dimensions.get("Upper Cut")
                Initial_Speed14 = nsolve(equation3 - Dimension1, V0, 10)
                result.append((Initial_Speed14, "Upper Cut"))
            if key == "Scoop":
                Dimension2 = Wankhede_dimensions.get("Scoop")
                Initial_Speed15 = nsolve(equation3 - Dimension2, V0, 10)
                result.append((Initial_Speed15, "Scoop"))
        if key == "Cover Drive" or key == "Cut":
            equation2 = (
    (V0 * cos(theta) + v_wind_x) * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) + v_wind_x) * k * (2 * (V0 * sin(theta) + v_wind_y) / ((V0 * sin(theta) + v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g)
            )
            if key == "Cover Drive" :
                Dimension5 = Wankhede_dimensions.get("Cover Drive")
                Initial_Speed16 = nsolve(equation2 - Dimension5, V0, 10)
                result.append((Initial_Speed16, "Cover Drive"))
            if key == "Cut":
                Dimension6 = Wankhede_dimensions.get("Cut")
                Initial_Speed17 = nsolve(equation2 - Dimension6, V0, 10)
                result.append((Initial_Speed17, "Cut"))
        if key == "Pull":
            equation1 =  (
    (V0 * cos(theta) - v_wind_x) * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) - v_wind_x) * k * (2 * (V0 * sin(theta) - v_wind_y) / ((V0 * sin(theta) - v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g)
)
            Dimension7 = Wankhede_dimensions.get("Pull")
            Initial_Speed18 = nsolve(equation1 - Dimension7, V0, 10)
            result.append((Initial_Speed18, "Pull"))

if User2 == "West to East":
    for key in Wankhede_dimensions:
        for key in Wankhede_dimensions:
            if key == "Upper Cut" or key == "Scoop" or key == "Long on Lofted" or key == "Straight Drive":
                equation3 =  (
    (V0 * cos(theta) ) * (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g) 
    - 0.5 * (V0 * cos(theta) ) * k * (2 * (V0 * sin(theta) ) / ((V0 * sin(theta) ) * k + g))**2 
    +  (2 * (V0 * sin(theta) )) / ((V0 * sin(theta) ) * k + g)
            )
                if key == "Straight Drive":
                    Dimension3 = Wankhede_dimensions.get("Straight Drive")
                    Initial_Speed12 = nsolve(equation3 - Dimension3, V0, 10)
                    result.append((Initial_Speed12, "Straight Drive"))
                if key == "Long on Lofted":
                    Dimension4 = Wankhede_dimensions.get("Long on Lofted")
                    Initial_Speed13 = nsolve(equation3 - Dimension4, V0, 10)
                    result.append((Initial_Speed13, "Long on Lofted"))
                if key == "Upper Cut":
                    Dimension1 = Wankhede_dimensions.get("Upper Cut")
                    Initial_Speed14 = nsolve(equation3 - Dimension1, V0, 10)
                    result.append((Initial_Speed14, "Upper Cut"))
                if key == "Scoop":
                    Dimension2 = Wankhede_dimensions.get("Scoop")
                    Initial_Speed15 = nsolve(equation3 - Dimension2, V0, 10)
                    result.append((Initial_Speed15, "Scoop"))
            if key == "Cover Drive" or key == "Cut":
                equation1 =  (
    (V0 * cos(theta) - v_wind_x) * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) - v_wind_x) * k * (2 * (V0 * sin(theta) - v_wind_y) / ((V0 * sin(theta) - v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) - v_wind_y)) / ((V0 * sin(theta) - v_wind_y) * k + g)
)
                if key == "Cover Drive" :
                    Dimension5 = Wankhede_dimensions.get("Cover Drive")
                    Initial_Speed18 = nsolve(equation1 - Dimension5, V0, 10)
                    result.append((Initial_Speed18, "Cover Drive"))
                if key == "Cut":
                    Dimension6 = Wankhede_dimensions.get("Cut")
                    Initial_Speed19 = nsolve(equation1 - Dimension6, V0, 10)
                    result.append((Initial_Speed19, "Cut"))
            if key == "Pull":
                equation2 = (
    (V0 * cos(theta) + v_wind_x) * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g) 
    - 0.5 * (V0 * cos(theta) + v_wind_x) * k * (2 * (V0 * sin(theta) + v_wind_y) / ((V0 * sin(theta) + v_wind_y) * k + g))**2 
    + v_wind_x * (2 * (V0 * sin(theta) + v_wind_y)) / ((V0 * sin(theta) + v_wind_y) * k + g)
            )
                Dimension7 = Wankhede_dimensions.get("Pull")
                Initial_Speed20 = nsolve(equation2 - Dimension7, V0, 10)
                result.append((Initial_Speed20, "Pull"))
                

                
min_value, min_key = min(result, key=lambda x: x[0])  # Extract the tuple with the min V0 value
print(f"The minimum V0 value is {min_value}, which corresponds to the shot '{min_key}'.")