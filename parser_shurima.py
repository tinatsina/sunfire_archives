class Parser:

    # ==================================== #
    # Variables to be put into the dataset #
    # ==================================== #

    COL_001_GAME_ID = ""
    COL_002_BLUE_WIN = ""
    COL_003_BLUE_KILLS = -1
    COL_004_RED_KILLS = -1
    COL_005_BLUE_DEATHS = -1
    COL_006_RED_DEATHS = -1
    COL_007_RED_ASSISTS = -1
    COL_008_BLUE_ASSISTS = -1
    COL_009_BLUE_WARDS_PLACED = -1
    COL_010_RED_WARDS_PLACED = -1
    COL_011_BLUE_WARDS_DESTROYED = -1
    COL_012_RED_WARDS_DESTROYED = -1
    COL_013_BLUE_DRAGONS = -1
    COL_014_RED_DRAGONS = -1
    COL_015_BLUE_BARONS = -1
    COL_016_RED_BARONS = -1
    COL_017_BLUE_TOWERS = -1
    COL_018_RED_TOWERS = -1
    COL_019_BLUE_ELITE_MONSTERS = -1
    COL_020_RED_ELITE_MONSTERS = -1
    COL_021_BLUE_TEAM_GOLD = -1
    COL_022_RED_TEAM_GOLD = -1
    COL_023_BLUE_TEAM_LEVEL = -1
    COL_024_RED_TEAM_LEVEL = -1
    COL_025_BLUE_TEAM_CS = -1
    COL_026_RED_TEAM_CS = -1
    COL_027_BLUE_TEAAM_CS_PER_MINUTE = -1
    COL_028_RED_TEAAM_CS_PER_MINUTE = -1
    COL_029_BLUE_GOLD_DIFF = -1
    COL_030_RED_GOLD_DIFF = -1
    COL_031_BLUE_GOLD_PER_MIN = -1
    COL_032_RED_GOLD_PER_MIN = -1
    COL_033_BLUE_TEAM_TOP = ""
    COL_034_BLUE_TEAM_JNG = ""
    COL_035_BLUE_TEAM_MID = ""
    COL_036_BLUE_TEAM_ADC = ""
    COL_037_BLUE_TEAM_SUP = ""
    COL_038_RED_TEAM_TOP = ""
    COL_039_RED_TEAM_JNG = ""
    COL_040_RED_TEAM_MID = ""
    COL_041_RED_TEAM_ADC = ""
    COL_042_RED_TEAM_SUP = ""

    COL_043_BLLUE_TEAM_TOP_ITEM_1 = ""
    COL_044_BLLUE_TEAM_TOP_ITEM_2 = ""
    COL_045_BLLUE_TEAM_TOP_ITEM_3 = ""
    COL_046_BLLUE_TEAM_TOP_ITEM_4 = ""
    COL_047_BLLUE_TEAM_TOP_ITEM_5 = ""
    COL_048_BLLUE_TEAM_TOP_ITEM_6 = ""
    COL_049_BLLUE_TEAM_TOP_ITEM_VISION = ""

    COL_050_BLLUE_TEAM_JNG_ITEM_1 = ""
    COL_051_BLLUE_TEAM_JNG_ITEM_2 = ""
    COL_052_BLLUE_TEAM_JNG_ITEM_3 = ""
    COL_053_BLLUE_TEAM_JNG_ITEM_4 = ""
    COL_054_BLLUE_TEAM_JNG_ITEM_5 = ""
    COL_055_BLLUE_TEAM_JNG_ITEM_6 = ""
    COL_056_BLLUE_TEAM_JNG_ITEM_VISION = ""

    COL_057_BLLUE_TEAM_MID_ITEM_1 = ""
    COL_058_BLLUE_TEAM_MID_ITEM_2 = ""
    COL_059_BLLUE_TEAM_MID_ITEM_3 = ""
    COL_060_BLLUE_TEAM_MID_ITEM_4 = ""
    COL_061_BLLUE_TEAM_MID_ITEM_5 = ""
    COL_062_BLLUE_TEAM_MID_ITEM_6 = ""
    COL_063_BLLUE_TEAM_MID_ITEM_VISION = ""

    COL_064_BLLUE_TEAM_ADC_ITEM_1 = ""
    COL_065_BLLUE_TEAM_ADC_ITEM_2 = ""
    COL_066_BLLUE_TEAM_ADC_ITEM_3 = ""
    COL_067_BLLUE_TEAM_ADC_ITEM_4 = ""
    COL_068_BLLUE_TEAM_ADC_ITEM_5 = ""
    COL_069_BLLUE_TEAM_ADC_ITEM_6 = ""
    COL_070_BLLUE_TEAM_ADC_ITEM_VISION = ""

    COL_070_BLLUE_TEAM_SUP_ITEM_1 = ""
    COL_071_BLLUE_TEAM_SUP_ITEM_2 = ""
    COL_072_BLLUE_TEAM_SUP_ITEM_3 = ""
    COL_073_BLLUE_TEAM_SUP_ITEM_4 = ""
    COL_074_BLLUE_TEAM_SUP_ITEM_5 = ""
    COL_075_BLLUE_TEAM_SUP_ITEM_6 = ""
    COL_076_BLLUE_TEAM_SUP_ITEM_VISION = ""

    COL_077_RED_TEAM_TOP_ITEM_1 = ""
    COL_078_RED_TEAM_TOP_ITEM_2 = ""
    COL_079_RED_TEAM_TOP_ITEM_3 = ""
    COL_080_RED_TEAM_TOP_ITEM_4 = ""
    COL_081_RED_TEAM_TOP_ITEM_5 = ""
    COL_082_RED_TEAM_TOP_ITEM_6 = ""
    COL_083_RED_TEAM_TOP_ITEM_VISION = ""

    COL_084_RED_TEAM_JNG_ITEM_1 = ""
    COL_085_RED_TEAM_JNG_ITEM_2 = ""
    COL_086_RED_TEAM_JNG_ITEM_3 = ""
    COL_087_RED_TEAM_JNG_ITEM_4 = ""
    COL_088_RED_TEAM_JNG_ITEM_5 = ""
    COL_089_RED_TEAM_JNG_ITEM_6 = ""
    COL_090_RED_TEAM_JNG_ITEM_VISION = ""

    COL_091_RED_TEAM_MID_ITEM_1 = ""
    COL_092_RED_TEAM_MID_ITEM_2 = ""
    COL_093_RED_TEAM_MID_ITEM_3 = ""
    COL_094_RED_TEAM_MID_ITEM_4 = ""
    COL_095_RED_TEAM_MID_ITEM_5 = ""
    COL_096_RED_TEAM_MID_ITEM_6 = ""
    COL_097_RED_TEAM_MID_ITEM_VISION = ""

    COL_098_RED_TEAM_ADC_ITEM_1 = ""
    COL_099_RED_TEAM_ADC_ITEM_2 = ""
    COL_100_RED_TEAM_ADC_ITEM_3 = ""
    COL_101_RED_TEAM_ADC_ITEM_4 = ""
    COL_102_RED_TEAM_ADC_ITEM_5 = ""
    COL_103_RED_TEAM_ADC_ITEM_6 = ""
    COL_104_RED_TEAM_ADC_ITEM_VISION = ""

    COL_105_RED_TEAM_SUP_ITEM_1 = ""
    COL_106_RED_TEAM_SUP_ITEM_2 = ""
    COL_107_RED_TEAM_SUP_ITEM_3 = ""
    COL_108_RED_TEAM_SUP_ITEM_4 = ""
    COL_109_RED_TEAM_SUP_ITEM_5 = ""
    COL_110_RED_TEAM_SUP_ITEM_6 = ""
    COL_111_RED_TEAM_SUP_ITEM_VISION = ""

    COL_112_BLUE_TEAM_TOP_SUMMONER_01 = ""
    COL_113_BLUE_TEAM_TOP_SUMMONER_02 = ""
    COL_114_BLUE_TEAM_JNG_SUMMONER_01 = ""
    COL_115_BLUE_TEAM_JNG_SUMMONER_02 = ""
    COL_116_BLUE_TEAM_MID_SUMMONER_01 = ""
    COL_117_BLUE_TEAM_MID_SUMMONER_02 = ""
    COL_118_BLUE_TEAM_ADC_SUMMONER_01 = ""
    COL_119_BLUE_TEAM_ADC_SUMMONER_02 = ""
    COL_120_BLUE_TEAM_SUP_SUMMONER_01 = ""
    COL_121_BLUE_TEAM_SUP_SUMMONER_02 = ""

    COL_122_RED_TEAM_TOP_SUMMONER_01 = ""
    COL_123_RED_TEAM_TOP_SUMMONER_02 = ""
    COL_124_RED_TEAM_JNG_SUMMONER_01 = ""
    COL_125_RED_TEAM_JNG_SUMMONER_02 = ""
    COL_126_RED_TEAM_MID_SUMMONER_01 = ""
    COL_127_RED_TEAM_MID_SUMMONER_02 = ""
    COL_128_RED_TEAM_ADC_SUMMONER_01 = ""
    COL_129_RED_TEAM_ADC_SUMMONER_02 = ""
    COL_130_RED_TEAM_SUP_SUMMONER_01 = ""
    COL_131_RED_TEAM_SUP_SUMMONER_02 = ""

    # ======================================= #
    # List and Definitions of XPath variables #
    # ======================================= #
    WIN_TEAM = '//*[@id="__next"]/div[5]/div/div[2]/div[1]/table[1]/thead/tr/th[1]'
    KILLS_LEFT = '//*[@id="__next"]/div[5]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]'
    KILLS_RIGHT = '//*[@id="__next"]/div[5]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[3]'
    KDA_A1 = '//*[@id="__next"]/div[5]/div/div[2]/div[1]/table[1]/tbody/tr[1]/td[6]/div[1]'
    WARDS = '//*[@id="__next"]/div[5]/div/div[2]/div[1]/table[1]/tbody/tr[1]/td[8]/div'
    GOLD_LEFT = '//*[@id="__next"]/div[5]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]'
    GOLD_RIGHT = '//*[@id="__next"]/div[5]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[3]'

    # ===================================== #
    # Special variables for deriving values #
    # ===================================== #
    VICTORY_RED_TEAM = "Victory(Red team)"
    VICTORY_BLUE_TEAM = "Victory(Blue team)"
    DEFEAT_RED_TEAM = "Defeat(Red team)"
    DEFEAT_BLUE_TEAM = "Defeat(Blue team)"

    # ===================================== #
    # Specialised Data Collection Functions #
    # ===================================== #
    def get_blue_win_status(self, winning_team):
        if winning_team == self.VICTORY_BLUE_TEAM:
            return 1
        elif winning_team == self.VICTORY_RED_TEAM:
            return 0
        elif winning_team == self.DEFEAT_RED_TEAM:
            return 1
        elif winning_team == self.DEFEAT_BLUE_TEAM:
            return 0
        
    def get_total_kills(self, winning_team, kills_left, kills_right):
        result = [-1,-1]
        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = kills_left
            result[1] = kills_right
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = kills_left
            result[0] = kills_right
        
        return result
    
    def parse_kda_data_deaths(self,kda):
        result = []
        for x in kda:
            temp = x.split("/")
            result.append(int(temp[1]))

        return result
    
    def parse_kda_data_assists(self,kda):
        result = []
        for x in kda:
            temp = x.split("/")
            final = temp[2].split(" ")
            result.append(int(final[0]))

        return result
    
    def parse_ward_data_placed(self,ward):
        result = []

        for x in ward:
            temp = x.split(" / ")
            result.append(int(temp[0]))

        return result
    
    def parse_ward_data_destroyed(self,ward):
        result = []

        for x in ward:
            temp = x.split(" / ")
            result.append(int(temp[1]))

        return result
    
    
    def get_team_deaths(self,winning_team,kda):
        result = [-1,-1]
        kda_list = self.parse_kda_data_deaths(kda)

        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = sum(kda_list[:5])
            result[1] = sum(kda_list[5:])
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = sum(kda_list[:5])
            result[0] = sum(kda_list[5:])

        return result

    def get_team_assists(self,winning_team,kda):
        kda_list = self.parse_kda_data_assists(kda)
        result = [-1,-1]
        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = sum(kda_list[:5])
            result[1] = sum(kda_list[5:])
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = sum(kda_list[:5])
            result[0] = sum(kda_list[5:])

        return result
    
    def get_team_wards_placed(self,winning_team,ward):
        ward_list = self.parse_ward_data_placed(ward)
        result = [-1,-1]
        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = sum(ward_list[:5])
            result[1] = sum(ward_list[5:])
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = sum(ward_list[:5])
            result[0] = sum(ward_list[5:])

        return result
    
    def get_team_wards_destroyed(self,winning_team,ward):
        ward_list = self.parse_ward_data_destroyed(ward)
        result = [-1,-1]
        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = sum(ward_list[:5])
            result[1] = sum(ward_list[5:])
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = sum(ward_list[:5])
            result[0] = sum(ward_list[5:])

        return result
    
    def get_team_objectives(self,winning_team,objectives):
        tmp_left = objectives[0].split("\n")
        tmp_right = objectives[1].split("\n")
        result = []

        for x in range(6):
            tmp_left[x] = int(tmp_left[x])
            tmp_right[x] = int(tmp_right[x])

        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result.append(tmp_left)
            result.append(tmp_right)
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result.append(tmp_right)
            result.append(tmp_left)

        return result
    
    def get_team_gold(self,winning_team,gold):
        result_tmp = []
        result = []
        for x in gold:
            tmp = int(x.replace(",",""))
            result_tmp.append(tmp)

        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result.append(result_tmp[0])
            result.append(result_tmp[1])
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result.append(result_tmp[1])
            result.append(result_tmp[0])

        return result

    def get_team_level(self,winning_team,level_list):
        levels_tmp = []

        for x in level_list:
            levels_tmp.append(int(x))

        levels = levels_tmp[2:]

        result = [-1,-1]

        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = sum(levels[:5])/5
            result[1] = sum(levels[5:])/5
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = sum(levels[:5])/5
            result[0] = sum(levels[5:])/5

        return result

    def get_team_total_cs(self,winning_team,cs_list):
        levels_temp = cs_list[1:]
        cs = []
        result = [-1,-1]

        for x in levels_temp:
            cs.append(int(x[0]))

        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = sum(cs[:5])
            result[1] = sum(cs[5:])
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = sum(cs[:5])
            result[0] = sum(cs[5:])

        return result
    
    def get_team_total_cs_per_minute(self,winning_team,cs_list):
        levels_temp = cs_list[1:]
        cs = []
        result = [-1,-1]

        for x in levels_temp:
            cs.append(float(x[1].replace("/m","")))


        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = sum(cs[:5])
            result[1] = sum(cs[5:])
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = sum(cs[:5])
            result[0] = sum(cs[5:])

        return result
    
    def get_total_game_time_minutes(self,cs_list):
        cs_temp = cs_list[1:]
        total_game_time = int(cs_temp[0][0])
        cs_per_minute = float(cs_temp[0][1].replace("/m",""))

        return total_game_time/cs_per_minute
    
    def get_team_champion_list(self,winning_team,champ_list):
        temp = champ_list[1:]
        result = [-1,-1]
        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = temp[:5]
            result[1] = temp[5:]
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = temp[:5]
            result[0] = temp[5:]
    
        return result
    
    def get_team_item_list(self,winning_team,item_list):
        result = [-1,-1]
        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = item_list[:5]
            result[1] = item_list[5:]
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = item_list[:5]
            result[0] = item_list[5:]
    
        return result
    
    def get_team_runes_list(self,winning_team,rune_list):
        result = [-1,-1]
        if winning_team == self.VICTORY_BLUE_TEAM or winning_team == self.DEFEAT_BLUE_TEAM:
            result[0] = rune_list[:5]
            result[1] = rune_list[5:]
        elif winning_team == self.VICTORY_RED_TEAM or winning_team == self.DEFEAT_RED_TEAM:
            result[1] = rune_list[:5]
            result[0] = rune_list[5:]

        return result
