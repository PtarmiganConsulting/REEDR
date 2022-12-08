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

            ln_of_crawl_adjust = -0.57831567002439 + 0.598333210175362*math.log(footprint) + -0.0339554160401319*math.log(total_envelope_height) + -0.00335138196797992*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -4.95189805160011 + 0.323089235151636*math.log(footprint) + 0.357954844729464*math.log(total_envelope_height) + 1.47837666394136*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.18936943365758 + 0.0640358403055768*math.log(footprint) + -0.0999325792341555*math.log(total_envelope_height) + 0.131563521887011*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.683820631214255 + 0.61523330083822*math.log(footprint) + -0.0378108768305732*math.log(total_envelope_height) + -0.0130367930108907*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

        else: #if ACH50 >9
            ln_of_living_adjust = -5.56586988439739 + 0.376293528194144*math.log(footprint) + 0.418430811611842*math.log(total_envelope_height) + 1.52439919409061*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.541665794835799 + 0.0748564756756913*math.log(footprint) + 0.00547899248162892*math.log(total_envelope_height) + 0.269358365472381*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            ln_of_crawl_adjust = -0.833135093128905 + 0.638219665153735*math.log(footprint) + -0.0405001563027068*math.log(total_envelope_height) + -0.0214967560735974*math.log(ACH50)
            crawl_adjust = math.exp(ln_of_crawl_adjust)

    elif foundation_type == "Unheated Basement":

        if ACH50 <= 3:
            ln_of_living_adjust = -4.0049211230694 + 0.29334006830038*math.log(footprint) + 0.308470008957762*math.log(total_envelope_height) + 1.02449589465282*math.log(ACH50)
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
            ln_of_living_adjust = -7.50760925775228 + 0.827974951892082*math.log(footprint) + 0.00316063420335651*math.log(total_envelope_height) + 1.4002739382372*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 1.23129226756326 + 0.0954891411911133*math.log(footprint) + -0.167483919772096*math.log(total_envelope_height) + 0.0481161923744135*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        elif ACH50 >3 and ACH50 <= 9:
            ln_of_living_adjust = -5.80562124716613 + 0.51823062303286*math.log(footprint) + 0.0672650682960535*math.log(total_envelope_height) + 1.754113322665*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.855140824123791 + 0.0920570038711215*math.log(footprint) + -0.0919666012731126*math.log(total_envelope_height) + 0.202647584023343*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

        else: #if ACH50 >9
            ln_of_living_adjust = -5.45020719790042 + 0.481827544334094*math.log(footprint) + 0.0933158986544682*math.log(total_envelope_height) + 1.70045883883582*math.log(ACH50)
            living_adjust = math.exp(ln_of_living_adjust)

            ln_of_attic_adjust = 0.389139840435075 + 0.096817467876815*math.log(footprint) + -0.0242709692178634*math.log(total_envelope_height) + 0.326247837260171*math.log(ACH50)
            attic_adjust = math.exp(ln_of_attic_adjust)

            crawl_adjust = 999

    adjust = [living_adjust, attic_adjust, crawl_adjust]
    
    return adjust