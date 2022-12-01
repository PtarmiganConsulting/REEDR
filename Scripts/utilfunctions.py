import math

def estimateInfiltrationAdjustment(foundation_type, ACH50, footprint, total_envelope_height):
    
    adjust = []

    if foundation_type == "Slab":

        if ACH50 <= 3:
            ln_of_living_adjust = -5.4794627405224 + 0.449575948578335*math.log(footprint) + 0.340049847086377*math.log(total_envelope_height) + 1.18718157939516*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.22025360352588 + 0.103901122852495*math.log(footprint) + -0.191999815003472*math.log(total_envelope_height) + 0.0270238487894906*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -5.41197321741644 + 0.357699043323076*math.log(footprint) + 0.374275258344276*math.log(total_envelope_height) + 1.54427322040671*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.00072104269842 + 0.105239273408532*math.log(footprint) + -0.148239350249268*math.log(total_envelope_height) + 0.10243804625756*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        else: #if ACH50 >9
            ln_of_living_adjust = -5.77021675553459 + 0.386814978635308*math.log(footprint) + 0.438267289039239*math.log(total_envelope_height) + 1.54963030520262*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.586835714792934 + 0.116480279346565*math.log(footprint) + -0.106070653271649*math.log(total_envelope_height) + 0.204471167997202*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

    elif foundation_type == "Vented Crawlspace":

        if ACH50 <= 3:
            ln_of_living_adjust = -4.56455900410368 + 0.375134782319205*math.log(footprint) + 0.283151523710581*math.log(total_envelope_height) + 1.0841939308996*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.50812524050211 + 0.0693245774269299*math.log(footprint) + -0.189692448468225*math.log(total_envelope_height) + 0.0165343649248096*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -3.11301672450909 + 0.953017577781788*math.log(footprint) + -0.193637552856871*math.log(total_envelope_height) + -0.0171712203051145*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -4.95189805160011 + 0.323089235151636*math.log(footprint) + 0.357954844729464*math.log(total_envelope_height) + 1.47837666394136*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.23236984996619 + 0.0833944085165425*math.log(footprint) + -0.155963910869687*math.log(total_envelope_height) + 0.0822558412936645*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -3.37792506121522 + 0.99870128356327*math.log(footprint) + -0.199021607621025*math.log(total_envelope_height) + -0.0656765423647718*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        else: #if ACH50 >9
            ln_of_living_adjust = -5.56586988439739 + 0.376293528194144*math.log(footprint) + 0.418430811611842*math.log(total_envelope_height) + 1.52439919409061*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.741546852616987 + 0.101587496608975*math.log(footprint) + -0.111624837473128*math.log(total_envelope_height) + 0.193420416840685*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -3.80216748574895 + 1.05873839622137*math.log(footprint) + -0.187043230186273*math.log(total_envelope_height) + -0.0919957928791571*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

    elif foundation_type == "Unheated Basement":

        if ACH50 <= 3:
            ln_of_living_adjust = -3.57769569818466 + 0.272836485392094*math.log(footprint) + 0.231498952713215*math.log(total_envelope_height) + 1.04385902311568*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.52572193845501 + 0.0674667407945934*math.log(footprint) + -0.190676412416758*math.log(total_envelope_height) + 0.016710075865255*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.502927123479851 + 0.592150516811344*math.log(footprint) + -0.0405106898706407*math.log(total_envelope_height) + -0.00401571279840261*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -4.89351918231486 + 0.319198071535125*math.log(footprint) + 0.357369610388076*math.log(total_envelope_height) + 1.46661556201398*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.25437056644377 + 0.0811237067352913*math.log(footprint) + -0.156849495214322*math.log(total_envelope_height) + 0.0813046453885181*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.595372532261744 + 0.607310713890337*math.log(footprint) + -0.0435308626899328*math.log(total_envelope_height) + -0.0145645436935371*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        else: #if ACH50 >9
            ln_of_living_adjust = -5.53520482885818 + 0.375588619399222*math.log(footprint) + 0.416030213110777*math.log(total_envelope_height) + 1.51847061521071*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.765939367399061 + 0.0999676027594624*math.log(footprint) + -0.113987516277714*math.log(total_envelope_height) + 0.191071847839204*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.708753684339778 + 0.624045642214939*math.log(footprint) + -0.043207188591865*math.log(total_envelope_height) + -0.0206362608653354*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

    else: #foundation_type == "Heated Basement":

        if ACH50 <= 3:
            ln_of_living_adjust = -6.78620407324239 + 0.742702330851408*math.log(footprint) + 0.0464210240608145*math.log(total_envelope_height) + 1.38337264823804*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.45286569923433 + 0.0859961347419132*math.log(footprint) + -0.226173534010802*math.log(total_envelope_height) + 0.000143183828527772*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -4.78691575226144 + 0.451749744241801*math.log(footprint) + -0.0477765172345581*math.log(total_envelope_height) + 1.92267889893149*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 2.70988698606031 + -0.0989138949791077*math.log(footprint) + 0.0243456610940152*math.log(total_envelope_height) + 0.255605719770032*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        else: #if ACH50 >9
            ln_of_living_adjust = -3.76088279400004 + 0.465256849630124*math.log(footprint) + -0.172379546705378*math.log(total_envelope_height) + 1.56674800546467*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 3.07466331207313 + -0.0358883632336235*math.log(footprint) + -0.093044492099691*math.log(total_envelope_height) + 0.00662973463769741*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

    adjust = [living_adjust, attic_adjust, crawl_adjust]
    
    return adjust