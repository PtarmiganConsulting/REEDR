#*******************************************************************************************************************************************************************

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************

def convert_WperFt2_to_WperM2(WperFt2):
    WperM2 = 10.76*WperFt2
    return WperM2

def convert_degF_to_degC(degF):
    degC = (degF-32)*5/9
    return degC

def convert_degC_to_degF(degC):
    degF = (degC*9/5)+32
    return degF

def convert_IP_Uvalue_to_SI_Uvalue(BtuPerHft2F):
    WperM2K = BtuPerHft2F*5.67446589738871
    return WperM2K

def convert_J_to_kWh(J):
    kWh = J*0.000000277778
    return kWh

def convert_J_to_therm(J):
    therm = J*0.00000000948043
    return therm

def convert_J_to_galLPG(J):
    gal = J*0.0000000099247861544414
    return gal    

def convert_W_to_Btuh(W):
    Btuh = W*3.41
    return Btuh

def convert_Btuh_to_W(Btuh):
    W = Btuh/3.41
    return W

def convert_ft_to_m(ft):
    if ft == "":
        m = ""
    else:
        m = ft/3.281
    return m

def convert_ft2_to_m2(ft2):
    m2 = ft2/10.764
    return m2

def convert_ft3_to_m3(ft3):
    m3 = ft3/35.315
    return m3

def convert_kW_to_ton(kW):
    ton = kW/3.517
    return ton

def convert_W_to_ton(W):
    ton = W/3516.8528420667
    return ton

def convert_CFM_to_m3PerSec(CFM):
    m3PerSec = CFM/2118.8799727596793
    return m3PerSec

def convert_in2_to_m2(in2):
    m2 = in2*0.00064516
    return m2