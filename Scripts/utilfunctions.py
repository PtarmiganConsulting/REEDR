import math

def estimateInfiltrationAdjustment(foundation_type, ACH50, footprint, total_envelope_height, \
    living_infiltration_coeff_dict, attic_infiltration_coeff_dict, crawl_infiltration_coeff_dict):
    
    adjust = []

    if ACH50 <= 3:
        adjustmentLookupID = foundation_type + "_Low"
    elif ACH50 >3 and ACH50 <= 9:
        adjustmentLookupID =  foundation_type + "_Med"
    else: #if ACH50 >9
        adjustmentLookupID =  foundation_type + "_High"

    living_intercept = living_infiltration_coeff_dict[adjustmentLookupID]["Intercept"]
    living_footprint_coeff = living_infiltration_coeff_dict[adjustmentLookupID]["coeff_footprint"]
    living_height_coeff = living_infiltration_coeff_dict[adjustmentLookupID]["coeff_height"]
    living_ACH_coeff = living_infiltration_coeff_dict[adjustmentLookupID]["coeff_ACH50"]

    ln_of_living_adjust = living_intercept + living_footprint_coeff*math.log(footprint) + \
        living_height_coeff*math.log(total_envelope_height) + living_ACH_coeff*math.log(ACH50)

    living_adjust = math.exp(ln_of_living_adjust)

    attic_intercept = attic_infiltration_coeff_dict[adjustmentLookupID]["Intercept"]
    attic_footprint_coeff = attic_infiltration_coeff_dict[adjustmentLookupID]["coeff_footprint"]
    attic_height_coeff = attic_infiltration_coeff_dict[adjustmentLookupID]["coeff_height"]
    attic_ACH_coeff = attic_infiltration_coeff_dict[adjustmentLookupID]["coeff_ACH50"]
    
    ln_of_attic_adjust = attic_intercept + attic_footprint_coeff*math.log(footprint) + \
        attic_height_coeff*math.log(total_envelope_height) + attic_ACH_coeff*math.log(ACH50)

    attic_adjust = math.exp(ln_of_attic_adjust)

    if foundation_type == "Vented Crawlspace" or foundation_type == "Unheated Basement":

        crawl_intercept = crawl_infiltration_coeff_dict[adjustmentLookupID]["Intercept"]
        crawl_footprint_coeff = crawl_infiltration_coeff_dict[adjustmentLookupID]["coeff_footprint"]
        crawl_height_coeff = crawl_infiltration_coeff_dict[adjustmentLookupID]["coeff_height"]
        crawl_ACH_coeff = crawl_infiltration_coeff_dict[adjustmentLookupID]["coeff_ACH50"]
        
        ln_of_crawl_adjust = crawl_intercept + crawl_footprint_coeff*math.log(footprint) + \
            crawl_height_coeff*math.log(total_envelope_height) + crawl_ACH_coeff*math.log(ACH50)

        crawl_adjust = math.exp(ln_of_crawl_adjust)

    else:
        crawl_adjust = 999

    adjust = [living_adjust, attic_adjust, crawl_adjust]
    
    return adjust