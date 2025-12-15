import pygame
import sys
import os
import json
import random
import math


WIDTH, HEIGHT = 800, 600
FPS = 60
ROUND_TIME_MS = 10_000
LIVES_START = 3
POINTS_PER_CORRECT = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
LIGHT_GRAY = (100, 100, 100)
YELLOW = (240, 210, 60)
RED = (220, 50, 50)
DARK_BLUE = (15, 20, 40)

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets", "flags")
HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscore.json")
HEART_IMAGE_PATH = os.path.join(ASSETS_DIR, "heart-2.png")
EXCLUDED_FLAG_FILES = {"heart-2.png"}


ISO_NAME_AND_DIFFICULTY = {
    
    "us": ("United States", 1),
    "gb": ("United Kingdom", 1),
    "de": ("Germany", 1),
    "fr": ("France", 1),
    "it": ("Italy", 1),
    "es": ("Spain", 1),
    "br": ("Brazil", 1),
    "ca": ("Canada", 1),
    "mx": ("Mexico", 1),
    "ru": ("Russia", 1),
    "cn": ("China", 1),
    "jp": ("Japan", 1),
    "in": ("India", 1),
    "au": ("Australia", 1),
    "za": ("South Africa", 1),
    "ar": ("Argentina", 1),
    "nl": ("Netherlands", 1),
    "se": ("Sweden", 1),
    "no": ("Norway", 1),
    "fi": ("Finland", 1),
    "dk": ("Denmark", 1),
    "pt": ("Portugal", 1),
    "be": ("Belgium", 1),
    "ch": ("Switzerland", 1),
    "kr": ("South Korea", 1),
    "sa": ("Saudi Arabia", 1),
    "tr": ("Turkey", 1),
    "ae": ("United Arab Emirates", 1),
    "sg": ("Singapore", 1),
    "nz": ("New Zealand", 1),
    "ie": ("Ireland", 1),
    "il": ("Israel", 1),
    "gr": ("Greece", 1),
    "pl": ("Poland", 1),
    "at": ("Austria", 1),
    "hu": ("Hungary", 1),
    "ro": ("Romania", 1),
    "bg": ("Bulgaria", 1),
    "ua": ("Ukraine", 1),
    "th": ("Thailand", 1),
    "my": ("Malaysia", 1),
    "id": ("Indonesia", 1),
    "ph": ("Philippines", 1),
    "ng": ("Nigeria", 1),
    "ke": ("Kenya", 1),
    "cl": ("Chile", 1),
    "co": ("Colombia", 1),
    "pe": ("Peru", 1),
    "ve": ("Venezuela", 1),

    
    "ad": ("Andorra", 2),
    "ae": ("United Arab Emirates", 2),
    "af": ("Afghanistan", 2),
    "ag": ("Antigua and Barbuda", 2),
    "ai": ("Anguilla", 2),
    "al": ("Albania", 2),
    "am": ("Armenia", 2),
    "ao": ("Angola", 2),
    "aq": ("Antarctica", 2),
    "as": ("American Samoa", 2),
    "aw": ("Aruba", 2),
    "ax": ("Aland Islands", 2),
    "az": ("Azerbaijan", 2),
    "ba": ("Bosnia and Herzegovina", 2),
    "bb": ("Barbados", 2),
    "bd": ("Bangladesh", 2),
    "bf": ("Burkina Faso", 2),
    "bh": ("Bahrain", 2),
    "bi": ("Burundi", 2),
    "bj": (("Benin"), 2),
    "bl": ("Saint Barthelemy", 2),
    "bm": ("Bermuda", 2),
    "bn": ("Brunei", 2),
    "bo": ("Bolivia", 2),
    "bq": ("Caribbean Netherlands", 2),
    "bs": ("Bahamas", 2),
    "bt": ("Bhutan", 2),
    "bv": ("Bouvet Island", 2),
    "bw": ("Botswana", 2),
    "by": ("Belarus", 2),
    "bz": ("Belize", 2),
    "cc": ("Cocos (Keeling) Islands", 2),
    "cd": ("Democratic Republic of the Congo", 2),
    "cf": ("Central African Republic", 2),
    "cg": ("Republic of the Congo", 2),
    "ci": ("Cote d'Ivoire", 2),
    "ck": ("Cook Islands", 2),
    "cm": ("Cameroon", 2),
    "cr": ("Costa Rica", 2),
    "cu": ("Cuba", 2),
    "cv": ("Cabo Verde", 2),
    "cw": ("Curacao", 2),
    "cx": ("Christmas Island", 2),
    "cy": ("Cyprus", 2),
    "cz": ("Czechia", 2),
    "dj": ("Djibouti", 2),
    "dm": ("Dominica", 2),
    "do": ("Dominican Republic", 2),
    "dz": ("Algeria", 2),
    "ec": ("Ecuador", 2),
    "ee": ("Estonia", 2),
    "eg": ("Egypt", 2),
    "eh": ("Western Sahara", 2),
    "er": ("Eritrea", 2),
    "et": ("Ethiopia", 2),
    "fj": ("Fiji", 2),
    "fk": ("Falkland Islands", 2),
    "fm": ("Micronesia", 2),
    "fo": ("Faroe Islands", 2),
    "ga": ("Gabon", 2),
    "gb-eng": ("England", 2),
    "gb-nir": ("Northern Ireland", 2),
    "gb-sct": ("Scotland", 2),
    "gb-wls": ("Wales", 2),
    "gd": ("Grenada", 2),
    "ge": ("Georgia", 2),
    "gf": ("French Guiana", 2),
    "gg": ("Guernsey", 2),
    "gh": ("Ghana", 2),
    "gi": ("Gibraltar", 2),
    "gl": ("Greenland", 2),
    "gm": ("Gambia", 2),
    "gn": ("Guinea", 2),
    "gp": ("Guadeloupe", 2),
    "gq": ("Equatorial Guinea", 2),
    "gr": ("Greece", 2),
    "gs": ("South Georgia and the South Sandwich Islands", 2),
    "gt": ("Guatemala", 2),
    "gu": ("Guam", 2),
    "gw": ("Guinea-Bissau", 2),
    "gy": ("Guyana", 2),
    "hk": ("Hong Kong", 2),
    "hm": ("Heard Island and McDonald Islands", 2),
    "hn": ("Honduras", 2),
    "hr": ("Croatia", 2),
    "ht": ("Haiti", 2),
    "im": ("Isle of Man", 2),
    "io": ("British Indian Ocean Territory", 2),
    "iq": ("Iraq", 2),
    "ir": ("Iran", 2),
    "is": ("Iceland", 2),
    "je": ("Jersey", 2),
    "jm": ("Jamaica", 2),
    "jo": ("Jordan", 2),
    "ke": ("Kenya", 2),
    "kg": ("Kyrgyzstan", 2),
    "kh": ("Cambodia", 2),
    "ki": ("Kiribati", 2),
    "km": ("Comoros", 2),
    "kn": ("Saint Kitts and Nevis", 2),
    "kp": ("North Korea", 2),
    "kw": ("Kuwait", 2),
    "ky": ("Cayman Islands", 2),
    "kz": ("Kazakhstan", 2),
    "la": ("Laos", 2),
    "lb": ("Lebanon", 2),
    "lc": ("Saint Lucia", 2),
    "li": ("Liechtenstein", 2),
    "lk": ("Sri Lanka", 2),
    "lr": ("Liberia", 2),
    "ls": ("Lesotho", 2),
    "lt": ("Lithuania", 2),
    "lu": ("Luxembourg", 2),
    "lv": ("Latvia", 2),
    "ly": ("Libya", 2),
    "ma": ("Morocco", 2),
    "mc": ("Monaco", 2),
    "md": ("Moldova", 2),
    "me": ("Montenegro", 2),
    "mf": ("Saint Martin", 2),
    "mg": ("Madagascar", 2),
    "mh": ("Marshall Islands", 2),
    "mk": ("North Macedonia", 2),
    "ml": ("Mali", 2),
    "mm": ("Myanmar", 2),
    "mn": ("Mongolia", 2),
    "mo": ("Macao", 2),
    "mp": ("Northern Mariana Islands", 2),
    "mq": ("Martinique", 2),
    "mr": ("Mauritania", 2),
    "ms": ("Montserrat", 2),
    "mt": ("Malta", 2),
    "mu": ("Mauritius", 2),
    "mv": ("Maldives", 2),
    "mw": ("Malawi", 2),
    "mz": ("Mozambique", 2),
    "na": ("Namibia", 2),
    "nc": ("New Caledonia", 2),
    "ne": ("Niger", 2),
    "nf": ("Norfolk Island", 2),
    "ng": ("Nigeria", 2),
    "ni": ("Nicaragua", 2),
    "np": ("Nepal", 2),
    "nr": ("Nauru", 2),
    "nu": ("Niue", 2),
    "om": ("Oman", 2),
    "pa": ("Panama", 2),
    "pf": ("French Polynesia", 2),
    "pg": ("Papua New Guinea", 2),
    "ph": ("Philippines", 2),
    "pk": ("Pakistan", 2),
    "pm": ("Saint Pierre and Miquelon", 2),
    "pn": ("Pitcairn Islands", 2),
    "pr": ("Puerto Rico", 2),
    "ps": ("Palestine", 2),
    "pw": ("Palau", 2),
    "py": ("Paraguay", 2),
    "qa": ("Qatar", 2),
    "re": ("Reunion", 2),
    "rs": ("Serbia", 2),
    "rw": ("Rwanda", 2),
    "sb": ("Solomon Islands", 2),
    "sc": ("Seychelles", 2),
    "sd": ("Sudan", 2),
    "sh": ("Saint Helena", 2),
    "si": ("Slovenia", 2),
    "sj": ("Svalbard and Jan Mayen", 2),
    "sk": ("Slovakia", 2),
    "sl": ("Sierra Leone", 2),
    "sm": ("San Marino", 2),
    "sn": ("Senegal", 2),
    "so": ("Somalia", 2),
    "sr": ("Suriname", 2),
    "ss": ("South Sudan", 2),
    "st": ("Sao Tome and Principe", 2),
    "sv": ("El Salvador", 2),
    "sx": ("Sint Maarten", 2),
    "sy": ("Syria", 2),
    "sz": ("Eswatini", 2),
    "tc": ("Turks and Caicos Islands", 2),
    "td": ("Chad", 2),
    "tf": ("French Southern Territories", 2),
    "tg": ("Togo", 2),
    "tj": ("Tajikistan", 2),
    "tk": ("Tokelau", 2),
    "tl": ("Timor-Leste", 2),
    "tm": ("Turkmenistan", 2),
    "tn": ("Tunisia", 2),
    "to": ("Tonga", 2),
    "tt": ("Trinidad and Tobago", 2),
    "tv": ("Tuvalu", 2),
    "tw": ("Taiwan", 2),
    "tz": ("Tanzania", 2),
    "ug": ("Uganda", 2),
    "um": ("U.S. Outlying Islands", 2),
    "uy": ("Uruguay", 2),
    "uz": ("Uzbekistan", 2),
    "va": ("Vatican City", 2),
    "vc": ("Saint Vincent and the Grenadines", 2),
    "vg": ("British Virgin Islands", 2),
    "vi": ("U.S. Virgin Islands", 2),
    "vn": ("Vietnam", 2),
    "vu": ("Vanuatu", 2),
    "wf": ("Wallis and Futuna", 2),
    "ws": ("Samoa", 2),
    "xk": ("Kosovo", 2),
    "ye": ("Yemen", 2),
    "yt": ("Mayotte", 2),
    "zm": ("Zambia", 2),
    "zw": ("Zimbabwe", 2),

}


def build_countries_from_assets():
    countries = []
    if not os.path.isdir(ASSETS_DIR):
        return countries
    for entry in os.listdir(ASSETS_DIR):
        if not entry.lower().endswith(".png"):
            continue
        if entry in EXCLUDED_FLAG_FILES:
            continue
        code = entry[:-4].lower()
        info = ISO_NAME_AND_DIFFICULTY.get(code)
        if info is not None:
            name, difficulty = info
        else:
            name = code.upper()
            difficulty = 3
        countries.append(
            {
                "code": code,
                "name": name,
                "flag": os.path.join(ASSETS_DIR, entry),
                "difficulty": difficulty,
            }
        )
    return countries


COUNTRIES = build_countries_from_assets()


def load_high_score(path: str) -> int:
    if not os.path.exists(path):
        return 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "high_score" in data:
            return int(data["high_score"])
        if isinstance(data, int):
            return int(data)
    except Exception:
        return 0
    return 0


def save_high_score(path: str, score: int) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"high_score": int(score)}, f)
    except Exception:
        pass


def load_flag_image(path: str, size=(320, 220)) -> pygame.Surface:
    surface = pygame.Surface(size)
    surface.fill(DARK_BLUE)
    try:
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.smoothscale(img, size)
            return img
    except Exception:
        pass
    return surface


def load_heart_image(size=(32, 32)) -> pygame.Surface:
    surface = pygame.Surface(size, pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))
    try:
        if os.path.exists(HEART_IMAGE_PATH):
            img = pygame.image.load(HEART_IMAGE_PATH).convert_alpha()
            img = pygame.transform.smoothscale(img, size)
            return img
    except Exception:
        pass
    pygame.draw.circle(surface, RED, (size[0] // 3, size[1] // 3), min(size) // 4)
    pygame.draw.circle(surface, RED, (2 * size[0] // 3, size[1] // 3), min(size) // 4)
    points = [
        (size[0] // 6, size[1] // 3),
        (5 * size[0] // 6, size[1] // 3),
        (size[0] // 2, size[1] * 5 // 6),
    ]
    pygame.draw.polygon(surface, RED, points)
    return surface


def get_difficulty_for_round(round_number: int) -> int:
    if round_number <= 5:
        return 1
    if round_number <= 10:
        return 2
    return 3


def generate_question(round_number: int):
    difficulty = get_difficulty_for_round(round_number)
    available = [c for c in COUNTRIES if c["difficulty"] == difficulty]
    if not available:
        available = COUNTRIES[:]
    correct_country = random.choice(available)

    others = [c for c in COUNTRIES if c["name"] != correct_country["name"]]
    if len(others) >= 3:
        wrong_options = random.sample(others, 3)
    else:
        wrong_options = others
        while len(wrong_options) < 3 and COUNTRIES:
            candidate = random.choice(COUNTRIES)
            if candidate["name"] != correct_country["name"] and candidate not in wrong_options:
                wrong_options.append(candidate)

    options = [correct_country] + wrong_options
    random.shuffle(options)
    correct_index = options.index(correct_country)
    return correct_country, options, correct_index


def format_time_remaining(ms_left: int) -> str:
    seconds = max(0, ms_left) / 1000.0
    return f"{math.ceil(seconds):d}"


def draw_text(surface, text, font, color, center=None, topleft=None):
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center is not None:
        rect.center = center
    if topleft is not None:
        rect.topleft = topleft
    surface.blit(img, rect)
    return rect


def draw_game(screen, fonts, state):
    screen.fill(DARK_BLUE)

    x = 20
    y = 10
    heart_img = state.get("heart_image")
    if heart_img is not None:
        heart_rect = heart_img.get_rect()
        for i in range(state["lives"]):
            rect = heart_rect.copy()
            rect.topleft = (x + i * (rect.width + 6), y)
            screen.blit(heart_img, rect)
    else:
        lives_text = "Lives: " + ("❤" * state["lives"])
        draw_text(screen, lives_text, fonts["small"], RED, topleft=(20, 15))

    elapsed = pygame.time.get_ticks() - state["round_start_time"]
    remaining_ms = max(0, ROUND_TIME_MS - elapsed)
    timer_text = "Time: " + format_time_remaining(remaining_ms)
    draw_text(screen, timer_text, fonts["small"], WHITE, center=(WIDTH // 2, 20))

    score_text = f"Score: {state['score']}"
    score_img = fonts["small"].render(score_text, True, YELLOW)
    score_rect = score_img.get_rect()
    score_rect.top = 15
    score_rect.right = WIDTH - 20
    screen.blit(score_img, score_rect)

    flag_surface = state["flag_image"]
    flag_rect = flag_surface.get_rect()
    flag_rect.center = (WIDTH // 2, HEIGHT // 2 - 60)
    screen.blit(flag_surface, flag_rect)

    draw_text(screen, "Guess the country", fonts["title"], WHITE, center=(WIDTH // 2, 80))

    option_width = WIDTH - 160
    option_height = 50
    start_y = HEIGHT - 220
    gap_y = 60

    for i, country in enumerate(state["options"]):
        x = (WIDTH - option_width) // 2
        y = start_y + i * gap_y
        rect = pygame.Rect(x, y, option_width, option_height)
        is_selected = (i == state["selected_index"])
        bg_color = YELLOW if is_selected else GRAY
        pygame.draw.rect(screen, bg_color, rect, border_radius=8)
        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)

        label = f"{i + 1}. {country['name']}"
        draw_text(screen, label, fonts["medium"], BLACK, center=rect.center)


def draw_game_over(screen, fonts, state):
    screen.fill(DARK_BLUE)

    draw_text(screen, "GAME OVER", fonts["title"], RED, center=(WIDTH // 2, HEIGHT // 2 - 120))

    draw_text(screen, f"Your Score: {state['score']}", fonts["medium"], WHITE, center=(WIDTH // 2, HEIGHT // 2 - 40))
    draw_text(screen, f"High Score: {state['high_score']}", fonts["medium"], YELLOW, center=(WIDTH // 2, HEIGHT // 2 + 20))

    draw_text(screen, "Press R to restart", fonts["small"], WHITE, center=(WIDTH // 2, HEIGHT // 2 + 100))
    draw_text(screen, "Press Q or ESC to quit", fonts["small"], WHITE, center=(WIDTH // 2, HEIGHT // 2 + 140))


def main():
    pygame.init()
    pygame.display.set_caption("Guess the Country")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    fonts = {
        "title": pygame.font.SysFont(None, 56),
        "medium": pygame.font.SysFont(None, 36),
        "small": pygame.font.SysFont(None, 28),
    }

    heart_image = load_heart_image()
    high_score = load_high_score(HIGHSCORE_FILE)

    state = {
        "lives": LIVES_START,
        "score": 0,
        "round": 1,
        "high_score": high_score,
        "game_over": False,
        "selected_index": 0,
        "heart_image": heart_image,
    }

    correct_country, options, correct_index = generate_question(state["round"])
    state["correct_index"] = correct_index
    state["options"] = options
    state["current_country"] = correct_country
    state["flag_image"] = load_flag_image(correct_country["flag"])    
    state["round_start_time"] = pygame.time.get_ticks()

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if not state["game_over"]:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        state["selected_index"] = (state["selected_index"] - 1) % len(state["options"])
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        state["selected_index"] = (state["selected_index"] + 1) % len(state["options"])
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        chosen_index = state["selected_index"]
                        if chosen_index == state["correct_index"]:
                            state["score"] += POINTS_PER_CORRECT
                        else:
                            state["lives"] -= 1

                        if state["lives"] <= 0:
                            state["game_over"] = True
                            if state["score"] > state["high_score"]:
                                state["high_score"] = state["score"]
                                save_high_score(HIGHSCORE_FILE, state["high_score"])
                        else:
                            state["round"] += 1
                            correct_country, options, correct_index = generate_question(state["round"])
                            state["correct_index"] = correct_index
                            state["options"] = options
                            state["current_country"] = correct_country
                            state["flag_image"] = load_flag_image(correct_country["flag"])
                            state["selected_index"] = 0
                            state["round_start_time"] = pygame.time.get_ticks()

                    elif event.key in (pygame.K_1, pygame.K_KP1):
                        chosen_index = 0
                        if chosen_index == state["correct_index"]:
                            state["score"] += POINTS_PER_CORRECT
                        else:
                            state["lives"] -= 1

                        if state["lives"] <= 0:
                            state["game_over"] = True
                            if state["score"] > state["high_score"]:
                                state["high_score"] = state["score"]
                                save_high_score(HIGHSCORE_FILE, state["high_score"])
                        else:
                            state["round"] += 1
                            correct_country, options, correct_index = generate_question(state["round"])
                            state["correct_index"] = correct_index
                            state["options"] = options
                            state["current_country"] = correct_country
                            state["flag_image"] = load_flag_image(correct_country["flag"])
                            state["selected_index"] = 0
                            state["round_start_time"] = pygame.time.get_ticks()

                    elif event.key in (pygame.K_2, pygame.K_KP2) and len(state["options"]) >= 2:
                        chosen_index = 1
                        if chosen_index == state["correct_index"]:
                            state["score"] += POINTS_PER_CORRECT
                        else:
                            state["lives"] -= 1

                        if state["lives"] <= 0:
                            state["game_over"] = True
                            if state["score"] > state["high_score"]:
                                state["high_score"] = state["score"]
                                save_high_score(HIGHSCORE_FILE, state["high_score"])
                        else:
                            state["round"] += 1
                            correct_country, options, correct_index = generate_question(state["round"])
                            state["correct_index"] = correct_index
                            state["options"] = options
                            state["current_country"] = correct_country
                            state["flag_image"] = load_flag_image(correct_country["flag"])
                            state["selected_index"] = 0
                            state["round_start_time"] = pygame.time.get_ticks()

                    elif event.key in (pygame.K_3, pygame.K_KP3) and len(state["options"]) >= 3:
                        chosen_index = 2
                        if chosen_index == state["correct_index"]:
                            state["score"] += POINTS_PER_CORRECT
                        else:
                            state["lives"] -= 1

                        if state["lives"] <= 0:
                            state["game_over"] = True
                            if state["score"] > state["high_score"]:
                                state["high_score"] = state["score"]
                                save_high_score(HIGHSCORE_FILE, state["high_score"])
                        else:
                            state["round"] += 1
                            correct_country, options, correct_index = generate_question(state["round"])
                            state["correct_index"] = correct_index
                            state["options"] = options
                            state["current_country"] = correct_country
                            state["flag_image"] = load_flag_image(correct_country["flag"])
                            state["selected_index"] = 0
                            state["round_start_time"] = pygame.time.get_ticks()

                    elif event.key in (pygame.K_4, pygame.K_KP4) and len(state["options"]) >= 4:
                        chosen_index = 3
                        if chosen_index == state["correct_index"]:
                            state["score"] += POINTS_PER_CORRECT
                        else:
                            state["lives"] -= 1

                        if state["lives"] <= 0:
                            state["game_over"] = True
                            if state["score"] > state["high_score"]:
                                state["high_score"] = state["score"]
                                save_high_score(HIGHSCORE_FILE, state["high_score"])
                        else:
                            state["round"] += 1
                            correct_country, options, correct_index = generate_question(state["round"])
                            state["correct_index"] = correct_index
                            state["options"] = options
                            state["current_country"] = correct_country
                            state["flag_image"] = load_flag_image(correct_country["flag"])
                            state["selected_index"] = 0
                            state["round_start_time"] = pygame.time.get_ticks()

                else:
                    if event.key == pygame.K_r:
                        state["lives"] = LIVES_START
                        state["score"] = 0
                        state["round"] = 1
                        state["game_over"] = False
                        state["selected_index"] = 0
                        correct_country, options, correct_index = generate_question(state["round"])
                        state["correct_index"] = correct_index
                        state["options"] = options
                        state["current_country"] = correct_country
                        state["flag_image"] = load_flag_image(correct_country["flag"])
                        state["round_start_time"] = pygame.time.get_ticks()
                    elif event.key in (pygame.K_q,):
                        running = False

        if not state["game_over"]:
            elapsed = pygame.time.get_ticks() - state["round_start_time"]
            if elapsed >= ROUND_TIME_MS:
                state["lives"] -= 1
                if state["lives"] <= 0:
                    state["game_over"] = True
                    if state["score"] > state["high_score"]:
                        state["high_score"] = state["score"]
                        save_high_score(HIGHSCORE_FILE, state["high_score"])
                else:
                    state["round"] += 1
                    correct_country, options, correct_index = generate_question(state["round"])
                    state["correct_index"] = correct_index
                    state["options"] = options
                    state["current_country"] = correct_country
                    state["flag_image"] = load_flag_image(correct_country["flag"])
                    state["selected_index"] = 0
                    state["round_start_time"] = pygame.time.get_ticks()

        if not state["game_over"]:
            draw_game(screen, fonts, state)
        else:
            draw_game_over(screen, fonts, state)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
