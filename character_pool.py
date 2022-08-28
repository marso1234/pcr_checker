class character_pool:

    def __init__(self, str1, str2, str3):
        str_ls = [str1, str2, str3]
        #Team Arrangements
        self.teams = []
        self.pool = []
        self.borrow = []
        self.boss = []
        self.damage = []
        #Add Related Characters to Pool
        for str_characters in str_ls:
            characters = str_characters.split(",")
            self.boss.append(characters.pop(0)) #Pop Boss Type
            self.damage.append(int(characters.pop(0))) #Pop Damage
            if len(characters) != 5:
                raise ValueError('Invalid Arguments !')
            #Still contains the star
            self.teams.append(characters)
            for character in characters:
                if character not in self.pool:
                    #Exclude Characters Not Owned
                    if '*' not in character:
                        self.pool.append(character)

    def get_repeated_characters(self, current, target):
        #Get First Repeated Character
        if current == target:
            return False
        else:
            for c in current:
                if c in target:
                    return c
            return False

    def check_valid(self):
        #Looping the whole team
        for i in range(len(self.teams)):
            #There is a chance to borrow a character for each time
            team = self.teams[i]
            borrow_chance = True
            for character in team:
                if '*' in character:
                    if borrow_chance:
                        #Consumming the borrow chance
                        print('Borrow Required',character)
                        self.borrow.append(character.replace('*',''))
                        borrow_chance = False
                        continue
                    else:
                        print('------------Impossible-------------------------------------------')
                        return False
                if character in self.pool:
                    self.pool.remove(character)
                else:
                    #Allow One time borrow if not consummed
                    if borrow_chance:
                        borrow_chance = False
                        print(team)
                        print('Borrow Required',character)
                        self.borrow.append(character)
                        continue
                    else:
                        #Not Possible
                        print('------------Impossible-------------------------------------------')
                        return False
            #Borrow Characters If borrow not being used
            if borrow_chance:
                for t2 in self.teams[i:]:
                    borrow = self.get_repeated_characters(team, t2)
                    if borrow:
                        print('Character Repeated, Borrow',borrow)
                        self.pool.append(borrow.replace('*',''))
                        self.borrow.append(borrow)
                        break
                print(borrow)
                #borrow anything if no repeated
                if not borrow:
                    print('No Character Repeated, Borrow',team[0])
                    self.pool.append(team[0])
                    self.borrow.append(team[0])
        print('-------------------Possible----------------------------')
        return True

    def print_stat(self):
        print('Character Pool: ',self.pool)
        for i in range(len(self.teams)):
            print(f'Team {i}: ',self.teams[i],end='\t')
            try:
                print('Borrow: ',self.borrow[i])
            except:
                print()
        
    def save_combination(self, filename):
        with open(filename, 'a') as output_file:
            for i in range(len(self.teams)):
                output_file.write(f'{self.boss[i]}王: {self.damage[i]} {self.teams[i]}\t')
                try:
                    output_file.write(f'借: {self.borrow[i]}\n')
                except:
                    output_file.write('\n')
            output_file.write(f'\n累積輸出: {self.damage_delt()}\n')
            output_file.write(f'累積分數: {self.score_delt()}\n')
            output_file.write('------------------------------------------------\n')

    def damage_delt(self):
        return sum(self.damage)

    def score_delt(self):
        sum = 0
        for i in range(len(self.boss)):
            sum += MULTIPLIER[int(self.boss[i])-1] * self.damage[i]
        return sum


#Constant
MULTIPLIER = [3.5,3.5,3.7,3.8,4.0]