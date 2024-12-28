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

        