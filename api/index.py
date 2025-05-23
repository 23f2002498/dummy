from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all CORS origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Student data dictionary
student_data = {
    "EKxkr": 85, "l8V1kKalD": 93, "RWEhWA": 8, "ppddvo6": 97, "0EpLO0O": 1,
    "Isn": 88, "FoglgP": 95, "scBV": 59, "H1q": 65, "fi6": 19,
    "LXp1": 72, "JDiKSzKr": 28, "nG": 34, "L": 8, "lXkG5C2vc": 89,
    "1ZyNqqj43": 89, "yy7nZfH": 97, "bWmJnr": 94, "7WJ4m884FG": 22,
    "2": 22, "OM": 59, "xsdzN": 84, "nPucxgUBh": 80, "f": 43,
    "4HMmNxu": 21, "1AdrZ8T6": 80, "YRGT": 97, "yB5YMOe": 61,
    "yM2Mc4nFT": 82, "9z7Yf2r4": 80, "nF": 47, "J3jqXyH": 48,
    "ygqHHvjE": 12, "Rv": 89, "PyfzyM": 77, "yCWEXS090": 24,
    "V4Xy": 67, "3QkLRt": 51, "ohQJxP": 93, "V54KzjKG": 39,
    "o683Bfmo7": 16, "yGwsbFu0": 13, "8oJ1": 44, "5CYcVlCWk4": 49,
    "kxMXY5zLy": 79, "AwXw7yPb6": 52, "rMsyaRxZ": 78, "hvPR0": 31,
    "D": 42, "8": 95, "HmB": 70, "fU2": 87, "pID2ffu": 18,
    "OTsmSiOwh": 55, "z04EZ5pr6g": 22, "0esIew": 93, "Q": 66,
    "z": 49, "Co7nvok6": 8, "CqeMe9cGE": 15, "hOqo7YNM": 43,
    "ouJ5uDg9gt": 76, "JUdAVZ": 13, "DvegIbw6": 51, "i": 40,
    "35Ts": 9, "3hjNF": 36, "3I9mKKQd": 64, "wnmqb": 19,
    "vuFExw": 57, "jZyRk": 20, "hrWx": 19, "SLBQ": 66,
    "21wURBJF": 79, "4": 87, "7Qm3": 62, "Vw8l": 38,
    "LO": 77, "TKm9DROpD": 67, "YYzsxxk4": 76, "8ixg7Ii": 40,
    "cwkd2Or6Z": 24, "R0ck7sdD": 11, "mF0": 41, "n3yIxdD": 59,
    "5": 82, "PuTealKl": 68, "C91VQ": 11, "GP7QGNa1T": 13,
    "z6yVuIe9Rb": 50, "x": 48, "N6": 66, "WbZ4Tc": 68,
    "i1bIQgleL": 22, "VuG7W": 20, "XU": 86, "Ll": 48,
    "rFz": 91, "Itel7ZOfz8": 11, "YkxZz": 72
}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_data.get(name, 0) for name in names]
    return JSONResponse(content={"marks": marks})
