from flask import Flask, request, jsonify

app = Flask(__name__)

# Store marks data as a dictionary
marks_data = {
    "mq7TKQE": 10, "MRX": 4, "A": 65, "uL": 61, "DSOJ71lk3": 63, "HAz": 51, "j67NbzHvxh": 31, 
    "ZyfnAZ": 79, "sg": 39, "C0MM4jhp2": 4, "FCZnWaBc": 55, "ay6FzPOno": 18, "JRt": 52, "n5": 57, 
    "97o0": 91, "uZTsy3qB": 97, "sK1YxZesa": 82, "lkk0uHX": 40, "ofahODZ": 25, "RiravUIX": 65, 
    "17HC7Ow": 28, "GHILh79UWU": 62, "RY8f1h": 60, "bKD": 64, "7b7": 1, "AEY1Mwl": 71, 
    "KYFyQK5fN8": 38, "3b": 33, "ZZrVnKWx": 81, "eAer7lO1xE": 50, "mQ": 95, "XGfaJx": 33, 
    "hkZ": 79, "5KWPl": 81, "jqqSjZx": 33, "cBz": 36, "6OvYmXNd": 24, "AZvpjjtu": 92, 
    "zpL3Ez": 65, "ut": 6, "XTA": 69, "bvX": 48, "fKqQMivTu": 83, "TA5K1iL2": 54, 
    "O438sEJ81i": 89, "mhLQN4": 18, "qkd0dfl2O": 60, "C3ob": 39, "A65WDDMp": 61, 
    "VNzalf": 38, "E5sx": 42, "W": 7, "an9jgoG": 0, "DtAr": 29, "eRSz": 71, "CTUlp": 71, 
    "C": 69, "8": 26, "SfOa": 21, "M40": 77, "ph3KgqJU": 65, "flFvYCtw": 99, "U": 92, 
    "OP": 92, "eBxPImfN": 18, "idbSK": 97, "vqd": 98, "qM9wWZM6a2": 52, "8BfpGgL": 17, 
    "AdC": 9, "0D": 7, "Hl": 92, "etrN0E8Uqt": 20, "jTi": 8, "F27nOQo": 68, "Jts87z": 7, 
    "Nfd1": 38, "z": 76, "Y1q6H": 58, "TbEa": 82, "tH": 86, "uYY": 93, "O87et00TuI": 17, 
    "hAQ": 29, "3HSf": 53, "w1Ri5b1m": 80, "WqTe8": 11, "kz4M54xdu": 7, "h7F96mD5": 43, 
    "LXGrm9": 26, "8UHnanf2OS": 35, "juB": 10, "6cibtp": 10, "yOUEQSG": 52, 
    "vWsZI598m": 85, "e": 2, "M": 6, "iLJ": 32, "0T0N": 32, "bg6By": 52
}

@app.route("/api", methods=["GET"])
def get_marks():
    # Get names from the query params
    names = request.args.getlist("name")

    # Fetch marks in the same order
    results = [marks_data.get(name, "Not Found") for name in names]

    return jsonify({"marks": results})

# Vercel requires this function
def handler(event, context):
    return app(event, context)
