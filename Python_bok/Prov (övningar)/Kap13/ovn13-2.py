class Position:
    def __init__(self):
        self.lat_gr = 0
        self.lat_min = 0
        self.lat_sek = 0
        self.lat_nord = False
        self.long_gr = 0
        self.long_min = 0
        self.long_sek = 0
        self.long_öst = False

    def __str__(self):
        s = f'Latitud {self.lat_gr}\u00b0{self.lat_min}\'{self.lat_sek}"'
        if self.lat_nord:
            s += 'N, '
        else:
            s += 'S, '
        s += f'Longitud {self.long_gr}\u00b0{self.long_min}\'{self.long_sek}"'
        if self.long_öst:
            s += 'Ö'
        else:
            s += 'V'
        return s


GOT = Position()
GOT.lat_gr = 57;  GOT.lat_min = 39;  GOT.lat_sek = 47;  GOT.lat_nord = True
GOT.long_gr = 12; GOT.long_min = 16; GOT.long_sek = 58; GOT.long_öst = True

ARN = Position()
ARN.lat_gr = 59;  ARN.lat_min = 24;  ARN.lat_sek = 52;  ARN.lat_nord = True
ARN.long_gr = 17; ARN.long_min = 55; ARN.long_sek = 18; ARN.long_öst = True

print('GOT:', GOT)
print('ARN:', ARN)