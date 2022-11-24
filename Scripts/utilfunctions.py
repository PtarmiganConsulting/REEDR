def estimateInfiltrationAdjustment(foundation_type, ACH50, footprint, stories):
    
    if foundation_type == "Slab":

        if ACH50 <= 1:
            adjust_onestory = 0.00018*footprint**0.83612
            adjust_oneandhalfstory = 0.00311*footprint**0.49706
            adjust_twostory = 0.00345*footprint**0.49706
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 1.5:
            adjust_onestory = 0.0005*footprint**0.79986
            adjust_oneandhalfstory = 0.00623*footprint**0.49914
            adjust_twostory = 0.00692*footprint**0.49914
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 2.5:
            adjust_onestory = 0.0147*footprint**0.4782
            adjust_oneandhalfstory = 0.0267*footprint**0.4028
            adjust_twostory = 0.0297*footprint**0.4028
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 3.5:
            adjust_onestory = 0.0555*footprint**0.3767
            adjust_oneandhalfstory = 0.0624*footprint**0.3767
            adjust_twostory = 0.0693*footprint**0.3767
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 4.5:
            adjust_onestory = 0.0755*footprint**0.3758
            adjust_oneandhalfstory = 0.126*footprint**0.3238
            adjust_twostory = 0.14*footprint**0.3238
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 5.5:
            adjust_onestory = 0.1155*footprint**0.366
            adjust_oneandhalfstory = 0.1607*footprint**0.3315
            adjust_twostory = 0.1908*footprint**0.32365
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 6.5:
            adjust_onestory = 0.1611*footprint**0.3563
            adjust_oneandhalfstory = 0.2029*footprint**0.3392
            adjust_twostory = 0.2552*footprint**0.3235
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 7.5:
            adjust_onestory = 0.1916*footprint**0.3553
            adjust_oneandhalfstory = 0.2604*footprint**0.3282
            adjust_twostory = 0.2994*footprint**0.3252
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 8.5:
            adjust_onestory = 0.2693*footprint**0.3491
            adjust_oneandhalfstory = 0.3623*footprint**0.3248
            adjust_twostory = 0.4452*footprint**0.3124
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 9.5:
            adjust_onestory = 0.30969*footprint**0.3469
            adjust_oneandhalfstory = 0.4229*footprint**0.3258
            adjust_twostory = 0.4802*footprint**0.31725
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 10.5:
            adjust_onestory = 0.3527*footprint**0.3447
            adjust_oneandhalfstory = 0.4524*footprint**0.3268
            adjust_twostory = 0.5257*footprint**0.3221
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 11.5:
            adjust_onestory = 0.4539*footprint**0.3501
            adjust_oneandhalfstory = 0.6039*footprint**0.3278
            adjust_twostory = 0.6489*footprint**0.334
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 12.5:
            adjust_onestory = 0.5058*footprint**0.3481
            adjust_oneandhalfstory = 0.6306*footprint**0.3349
            adjust_twostory = 0.6856*footprint**0.3399
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 13.5:
            adjust_onestory = 0.5391*footprint**0.35
            adjust_oneandhalfstory = 0.6638*footprint**0.342
            adjust_twostory = 0.7058*footprint**0.3502
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 14.5:
            adjust_onestory = 0.5788*footprint**0.35
            adjust_oneandhalfstory = 0.6945*footprint**0.342
            adjust_twostory = 0.732*footprint**0.3502
            adjust_threestory = 0.00018*footprint**0.83612

        if ACH50 <= 15.5:
            adjust_onestory = 0.616*footprint**0.3535
            adjust_oneandhalfstory = 0.7255*footprint**0.3491
            adjust_twostory = 0.7567*footprint**0.3605
            adjust_threestory = 0.00018*footprint**0.83612


    # if foundation_type == "Vented Crawlspace":

    # if foundation_type == "Unheated Basement":

    # if foundation_type == "Heated Basement":

    
    
    
    return adjust