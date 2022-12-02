import math

def estimateInfiltrationAdjustment(foundation_type, ACH50, footprint, total_envelope_height):
    
    adjust = []

    if foundation_type == "Slab":

        if ACH50 <= 3:
            ln_of_living_adjust = -5.4794627405224 + 0.449575948578335*math.log(footprint) + 0.340049847086377*math.log(total_envelope_height) + 1.18718157939516*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.20628561488316 + 0.104222656723588*math.log(footprint) + -0.186698734594057*math.log(total_envelope_height) + 0.0311213076551005*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -5.41197321741644 + 0.357699043323076*math.log(footprint) + 0.374275258344276*math.log(total_envelope_height) + 1.54427322040671*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.836341162706868 + 0.107221500554972*math.log(footprint) + -0.109468611331111*math.log(total_envelope_height) + 0.14375919670089*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        else: #if ACH50 >9
            ln_of_living_adjust = -5.77021675553459 + 0.386814978635308*math.log(footprint) + 0.438267289039239*math.log(total_envelope_height) + 1.54963030520262*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.210021808379302 + 0.115380560889372*math.log(footprint) + -0.00718866652033437*math.log(total_envelope_height) + 0.284454562866848*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

    elif foundation_type == "Vented Crawlspace":

        if ACH50 <= 3:
            ln_of_living_adjust = -4.56455900410368 + 0.375134782319205*math.log(footprint) + 0.283151523710581*math.log(total_envelope_height) + 1.0841939308996*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.58102134544365 + 0.05682517047341*math.log(footprint) + -0.17651399691023*math.log(total_envelope_height) + 0.0255147565251867*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -1.18929965485452 + 0.68651068206866*math.log(footprint) + -0.0703840392330436*math.log(total_envelope_height) + -0.00645057776680579*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -4.95189805160011 + 0.323089235151636*math.log(footprint) + 0.357954844729464*math.log(total_envelope_height) + 1.47837666394136*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.18936943365758 + 0.0640358403055768*math.log(footprint) + -0.0999325792341555*math.log(total_envelope_height) + 0.131563521887011*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -1.41910538584929 + 0.723491734694965*math.log(footprint) + -0.0795766219597931*math.log(total_envelope_height) + -0.0263903031848593*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        else: #if ACH50 >9
            ln_of_living_adjust = -5.56586988439739 + 0.376293528194144*math.log(footprint) + 0.418430811611842*math.log(total_envelope_height) + 1.52439919409061*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.541665794835799 + 0.0748564756756913*math.log(footprint) + 0.00547899248162892*math.log(total_envelope_height) + 0.269358365472381*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -1.73881593009879 + 0.77214633914482*math.log(footprint) + -0.0844179798513457*math.log(total_envelope_height) + -0.0432235436955832*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

    elif foundation_type == "Unheated Basement":

        if ACH50 <= 3:
            ln_of_living_adjust = -3.57769569818466 + 0.272836485392094*math.log(footprint) + 0.231498952713215*math.log(total_envelope_height) + 1.04385902311568*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.6054636121344 + 0.0539986426948462*math.log(footprint) + -0.177196676842448*math.log(total_envelope_height) + 0.025990856810172*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.0819476129537362 + 0.531571799551593*math.log(footprint) + -0.0106147046591054*math.log(total_envelope_height) + -0.00117380445863238*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -4.89351918231486 + 0.319198071535125*math.log(footprint) + 0.357369610388076*math.log(total_envelope_height) + 1.46661556201398*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.19506301644098 + 0.0636205769686148*math.log(footprint) + -0.100186946453521*math.log(total_envelope_height) + 0.130811075329455*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.105903565440005 + 0.535528403019468*math.log(footprint) + -0.0113518891287177*math.log(total_envelope_height) + -0.00402690614571452*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        else: #if ACH50 >9
            ln_of_living_adjust = -5.53520482885818 + 0.375588619399222*math.log(footprint) + 0.416030213110777*math.log(total_envelope_height) + 1.51847061521071*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.549378963778551 + 0.074516240809454*math.log(footprint) + 0.004815693684798*math.log(total_envelope_height) + 0.26814686727753*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.138301270286122 + 0.540410560453106*math.log(footprint) + -0.0113009258336327*math.log(total_envelope_height) + -0.00604037052112423*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

    else: #foundation_type == "Heated Basement":

        if ACH50 <= 3:
            ln_of_living_adjust = -7.36037172774158 + 0.808787066481509*math.log(footprint) + 0.016003682061174*math.log(total_envelope_height) + 1.40181025851803*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.23129226756326 + 0.0954891411911133*math.log(footprint) + -0.167483919772096*math.log(total_envelope_height) + 0.0481161923744135*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -5.39697508212085 + 0.482258269530736*math.log(footprint) + 0.0495421602077332*math.log(total_envelope_height) + 1.72811451704117*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.911128972674308 + 0.117993612663188*math.log(footprint) + -0.169273154771191*math.log(total_envelope_height) + 0.139082070615369*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        else: #if ACH50 >9
            ln_of_living_adjust = -5.25792830750376 + 0.486891658324829*math.log(footprint) + 0.0467516261900185*math.log(total_envelope_height) + 1.6682025751285*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.370950512927855 + 0.133904971804104*math.log(footprint) + -0.136208958078823*math.log(total_envelope_height) + 0.296826099697312*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

    adjust = [living_adjust, attic_adjust, crawl_adjust]
    
    return adjust