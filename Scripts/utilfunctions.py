import math

def estimateInfiltrationAdjustment(foundation_type, ACH50, footprint, total_envelope_height):
    
    if foundation_type == "Slab":

        if ACH50 <= 3:
            ln_of_adjust = -5.25423130767863 + 0.434321563880068*math.log(footprint) + 0.292118278381926*math.log(total_envelope_height) + 1.14931354692269*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_adjust = -5.10755505716061 + 0.337904186682084*math.log(footprint) + 0.340677905009743*math.log(total_envelope_height) + 1.50105956435103*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        else: #if ACH50 >9
            ln_of_adjust = -5.16229813732622 + 0.347452775998166*math.log(footprint) + 0.370120263805017*math.log(total_envelope_height) + 1.47337938521874*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

    elif foundation_type == "Vented Crawlspace":

        if ACH50 <= 3:
            ln_of_adjust = -4.20689327379813 + 0.287936686339404*math.log(footprint) + 0.38844080879801*math.log(total_envelope_height) + 1.05471802350946*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_adjust = -4.88641604221937 + 0.32255060048008*math.log(footprint) + 0.35375200259744*math.log(total_envelope_height) + 1.45218069710441*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        else: #if ACH50 >9
            ln_of_adjust = -4.83929661590943 + 0.338407316049042*math.log(footprint) + 0.354060157896184*math.log(total_envelope_height) + 1.39216836587085*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

    elif foundation_type == "Unheated Basement":

        if ACH50 <= 3:
            ln_of_adjust = -4.20689327379813 + 0.287936686339404*math.log(footprint) + 0.38844080879801*math.log(total_envelope_height) + 1.05471802350946*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_adjust = -4.88641604221937 + 0.32255060048008*math.log(footprint) + 0.35375200259744*math.log(total_envelope_height) + 1.45218069710441*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        else: #if ACH50 >9
            ln_of_adjust = -4.83929661590943 + 0.338407316049042*math.log(footprint) + 0.354060157896184*math.log(total_envelope_height) + 1.39216836587085*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

    else: #foundation_type == "Heated Basement":

        if ACH50 <= 3:
            ln_of_adjust = -4.4310647118618 + 0.481454409895352*math.log(footprint) + 0.0694514980033807*math.log(total_envelope_height) + 1.08233124982433*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_adjust = -4.7973279760463 + 0.459813442720349*math.log(footprint) + 0.0700608527257766*math.log(total_envelope_height) + 1.48962801290284*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)

        else: #if ACH50 >9
            ln_of_adjust = -4.58646443873161 + 0.452301315106102*math.log(footprint) + 0.0684910658567368*math.log(total_envelope_height) + 1.43704513965387*math.log(ACH50)
            adjust = math.exp(ln_of_adjust)
    
    return adjust