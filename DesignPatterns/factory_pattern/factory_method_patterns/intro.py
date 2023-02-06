

# product.py
class Section:
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

# creator.py
class Profile:
    def __init__(self):
        self.sections = []
        self.create_profile()

    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)


class instagram(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


class facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


if __name__ == "__main__":
    profile_type = input("생성할 프로필을 선택해 주세요 [Facebook or Instagram]")
    profile = eval(profile_type.lower())()
    print(f"계정 생성중,,,{type(profile).__name__}")
    print(f"계정 섹션 -- {profile.get_sections()}")
