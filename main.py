import flet as ft
import random
import time
import json
import os
import ssl
# Bu iki sətir bütün SSL yoxlamalarını tamamilə söndürür
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

os.environ['PYTHONHTTPSVERIFY'] = '0'

# 1. MƏLUMAT BAZASI (LEVEL 1 VƏ 2 TAM DOLUDUR)
DATA = {
    "Level 1": {
        "Step 1": [
            {"word": "APPLE", "correct": "alma", "all": ["alma", "armud", "banan"]},
            {"word": "BOOK", "correct": "kitab", "all": ["kitab", "dəftər", "qələm"]},
            {"word": "WATER", "correct": "su", "all": ["su", "çay", "süd"]},
            {"word": "BREAD", "correct": "çörək", "all": ["çörək", "pendir", "ət"]},
            {"word": "SCHOOL", "correct": "məktəb", "all": ["məktəb", "ev", "bağ"]},
            {"word": "TEACHER", "correct": "müəllim", "all": ["müəllim", "şagird", "həkim"]},
            {"word": "FRIEND", "correct": "dost", "all": ["dost", "düşmən", "qonşu"]},
            {"word": "MOTHER", "correct": "ana", "all": ["ana", "ata", "bacı"]},
            {"word": "FATHER", "correct": "ata", "all": ["ata", "qardaş", "oğul"]},
            {"word": "NIGHT", "correct": "gecə", "all": ["gecə", "səhər", "gün"]}
        ],
        "Step 2": [
            {"word": "CAR", "correct": "maşın", "all": ["maşın", "təyyarə", "gəmi"]},
            {"word": "DOG", "correct": "it", "all": ["it", "pişik", "at"]},
            {"word": "SUN", "correct": "günəş", "all": ["günəş", "ay", "ulduz"]},
            {"word": "TREE", "correct": "ağac", "all": ["ağac", "gül", "ot"]},
            {"word": "CITY", "correct": "şəhər", "all": ["şəhər", "kənd", "ölkə"]},
            {"word": "EYE", "correct": "göz", "all": ["göz", "burun", "qulaq"]},
            {"word": "HAND", "correct": "əl", "all": ["əl", "ayaq", "baş"]},
            {"word": "RED", "correct": "qırmızı", "all": ["qırmızı", "göy", "sarı"]},
            {"word": "WHITE", "correct": "ağ", "all": ["ağ", "qara", "boz"]},
            {"word": "TIME", "correct": "vaxt", "all": ["vaxt", "saat", "gün"]}
        ],
        "Step 3": [
            {"word": "BOY", "correct": "oğlan", "all": ["oğlan", "qız", "kişi"]},
            {"word": "GIRL", "correct": "qız", "all": ["qız", "oğlan", "qadın"]},
            {"word": "MAN", "correct": "kişi", "all": ["kişi", "qadın", "uşaq"]},
            {"word": "WOMAN", "correct": "qadın", "all": ["qadın", "kişi", "oğlan"]},
            {"word": "BABY", "correct": "körpə", "all": ["körpə", "uşaq", "yeniyetmə"]},
            {"word": "BROTHER", "correct": "qardaş", "all": ["qardaş", "bacı", "əmi"]},
            {"word": "SISTER", "correct": "bacı", "all": ["bacı", "qardaş", "xala"]},
            {"word": "NAME", "correct": "ad", "all": ["ad", "soyad", "imza"]},
            {"word": "HOUSE", "correct": "ev", "all": ["ev", "mənzil", "otaq"]},
            {"word": "ROOM", "correct": "otaq", "all": ["otaq", "həyət", "qapı"]}
        ],
        "Step 4": [
            {"word": "GREEN", "correct": "yaşıl", "all": ["yaşıl", "mavi", "sarı"]},
            {"word": "YELLOW", "correct": "sarı", "all": ["sarı", "qırmızı", "narıncı"]},
            {"word": "BLACK", "correct": "qara", "all": ["qara", "ağ", "boz"]},
            {"word": "BROWN", "correct": "qəhvəyi", "all": ["qəhvəyi", "çəhrayı", "bənövşəyi"]},
            {"word": "PEN", "correct": "qələm", "all": ["qələm", "karandaş", "kağız"]},
            {"word": "PAPER", "correct": "kağız", "all": ["kağız", "kitab", "dəftər"]},
            {"word": "STUDENT", "correct": "şagird", "all": ["şagird", "müəllim", "direktor"]},
            {"word": "CLASS", "correct": "sinif", "all": ["sinif", "məktəb", "dərs"]},
            {"word": "CHAIR", "correct": "stul", "all": ["stul", "masa", "divan"]},
            {"word": "TABLE", "correct": "masa", "all": ["masa", "stul", "çarpayı"]}
        ],
        "Step 5": [
            {"word": "ONE", "correct": "bir", "all": ["bir", "iki", "üç"]},
            {"word": "TEN", "correct": "on", "all": ["on", "beş", "doqquz"]},
            {"word": "BIG", "correct": "böyük", "all": ["böyük", "kiçik", "uzun"]},
            {"word": "SMALL", "correct": "kiçik", "all": ["kiçik", "böyük", "qısa"]},
            {"word": "HOT", "correct": "isti", "all": ["isti", "soyuq", "ilıq"]},
            {"word": "COLD", "correct": "soyuq", "all": ["soyuq", "isti", "sərin"]},
            {"word": "GOOD", "correct": "yaxşı", "all": ["yaxşı", "pis", "əla"]},
            {"word": "BAD", "correct": "pis", "all": ["pis", "yaxşı", "orta"]},
            {"word": "HAPPY", "correct": "xoşbəxt", "all": ["xoşbəxt", "qəmli", "əsəbi"]},
            {"word": "SAD", "correct": "qəmli", "all": ["qəmli", "şən", "gülərüz"]}
        ],
        "Step 6": [
            {"word": "FISH", "correct": "balıq", "all": ["balıq", "quş", "heyvan"]},
            {"word": "BIRD", "correct": "quş", "all": ["quş", "balıq", "ilan"]},
            {"word": "HORSE", "correct": "at", "all": ["at", "it", "inək"]},
            {"word": "COW", "correct": "inək", "all": ["inək", "qoyun", "keçi"]},
            {"word": "MILK", "correct": "süd", "all": ["süd", "su", "çay"]},
            {"word": "TEA", "correct": "çay", "all": ["çay", "qəhvə", "şirə"]},
            {"word": "COFFEE", "correct": "qəhvə", "all": ["qəhvə", "çay", "süd"]},
            {"word": "SUGAR", "correct": "şəkər", "all": ["şəkər", "duz", "un"]},
            {"word": "SALT", "correct": "duz", "all": ["duz", "şəkər", "yağ"]},
            {"word": "MEAT", "correct": "ət", "all": ["ət", "toyuq", "balıq"]}
        ],
        "Step 7": [
            {"word": "HEAD", "correct": "baş", "all": ["baş", "üz", "saç"]},
            {"word": "HAIR", "correct": "saç", "all": ["saç", "göz", "burun"]},
            {"word": "NOSE", "correct": "burun", "all": ["burun", "ağız", "qulaq"]},
            {"word": "MOUTH", "correct": "ağiz", "all": ["ağız", "dil", "diş"]},
            {"word": "FOOT", "correct": "ayaq", "all": ["ayaq", "əl", "barmaq"]},
            {"word": "ARM", "correct": "qol", "all": ["qol", "çiyin", "dirsək"]},
            {"word": "LEG", "correct": "qıç", "all": ["qıç", "diz", "ayaq"]},
            {"word": "BODY", "correct": "bədən", "all": ["bədən", "üzv", "sümük"]},
            {"word": "SICK", "correct": "xəstə", "all": ["xəstə", "sağlam", "yorgun"]},
            {"word": "DOCTOR", "correct": "həkim", "all": ["həkim", "tibb bacısı", "xəstə"]}
        ],
        "Step 8": [
            {"word": "STREET", "correct": "küçə", "all": ["küçə", "yol", "park"]},
            {"word": "ROAD", "correct": "yol", "all": ["yol", "körpü", "tunel"]},
            {"word": "BUS", "correct": "avtobus", "all": ["avtobus", "maşın", "taksi"]},
            {"word": "TRAIN", "correct": "qatar", "all": ["qatar", "metro", "təyyarə"]},
            {"word": "PLANE", "correct": "təyyarə", "all": ["təyyarə", "vertolyot", "gəmi"]},
            {"word": "BOAT", "correct": "qayıq", "all": ["qayıq", "gəmi", "yaxta"]},
            {"word": "TICKET", "correct": "bilet", "all": ["bilet", "pasport", "vizitka"]},
            {"word": "MONEY", "correct": "pul", "all": ["pul", "kart", "qəpik"]},
            {"word": "SHOP", "correct": "mağaza", "all": ["mağaza", "bazar", "apteka"]},
            {"word": "PRICE", "correct": "qiymət", "all": ["qiymət", "endirim", "pul"]}
        ],
        "Step 9": [
            {"word": "MORNING", "correct": "səhər", "all": ["səhər", "axşam", "günorta"]},
            {"word": "EVENING", "correct": "axşam", "all": ["axşam", "səhər", "gecə"]},
            {"word": "DAY", "correct": "gün", "all": ["gün", "ay", "il"]},
            {"word": "WEEK", "correct": "həftə", "all": ["həftə", "gün", "ay"]},
            {"word": "MONTH", "correct": "ay", "all": ["ay", "il", "həftə"]},
            {"word": "YEAR", "correct": "il", "all": ["il", "ay", "əsır"]},
            {"word": "TODAY", "correct": "bu gün", "all": ["bu gün", "sabah", "dünən"]},
            {"word": "TOMORROW", "correct": "sabah", "all": ["sabah", "dünən", "bu gün"]},
            {"word": "YESTERDAY", "correct": "dünən", "all": ["dünən", "bu gün", "sabah"]},
            {"word": "CLOCK", "correct": "saat", "all": ["saat", "vaxt", "dəqiqə"]}
        ],
        "Step 10": [
            {"word": "RUN", "correct": "qaçmaq", "all": ["qaçmaq", "yerimək", "durmaq"]},
            {"word": "WALK", "correct": "yerimək", "all": ["yerimək", "qaçmaq", "oturmaq"]},
            {"word": "SLEEP", "correct": "yatmaq", "all": ["yatmaq", "oyanmaq", "durmaq"]},
            {"word": "EAT", "correct": "yemək", "all": ["yemək", "içmək", "bişirmək"]},
            {"word": "DRINK", "correct": "içmək", "all": ["içmək", "yemək", "udmaq"]},
            {"word": "READ", "correct": "oxumaq", "all": ["oxumaq", "yazmaq", "baxmaq"]},
            {"word": "WRITE", "correct": "yazmaq", "all": ["yazmaq", "oxumaq", "dinləmək"]},
            {"word": "SPEAK", "correct": "danışmaq", "all": ["danışmaq", "susmaq", "gülmək"]},
            {"word": "LISTEN", "correct": "dinləmək", "all": ["dinləmək", "danışmaq", "görmək"]},
            {"word": "PLAY", "correct": "oynamaq", "all": ["oynamaq", "işləmək", "yatmaq"]}
        ]
    },
    "Level 2": {
        "Step 1": [
            {"word": "WINDOW", "correct": "pəncərə", "all": ["pəncərə", "qapı", "divar"]},
            {"word": "KITCHEN", "correct": "mətbəx", "all": ["mətbəx", "hamam", "otaq"]},
            {"word": "STAIRS", "correct": "pilləkən", "all": ["pilləkən", "lift", "dam"]},
            {"word": "GARDEN", "correct": "bağça", "all": ["bağça", "həyət", "meşə"]},
            {"word": "BRIDGE", "correct": "körpü", "all": ["körpü", "yol", "çay"]},
            {"word": "OFFICE", "correct": "ofis", "all": ["ofis", "bank", "zavod"]},
            {"word": "POLICE", "correct": "polis", "all": ["polis", "əsgər", "yanğınsöndürən"]},
            {"word": "VILLAGE", "correct": "kənd", "all": ["kənd", "şəhər", "ölkə"]},
            {"word": "BOTTLE", "correct": "şüşə", "all": ["şüşə", "stəkan", "qab"]},
            {"word": "KNIFE", "correct": "bıçaq", "all": ["bıçaq", "qaşıq", "çəngəl"]}
        ],"Step 2": [
            {"word": "SHIRT", "correct": "köynək", "all": ["köynək", "şalvar", "ayaqqabı"]},
            {"word": "PANTS", "correct": "şalvar", "all": ["şalvar", "paltar", "corab"]},
            {"word": "SHOES", "correct": "ayaqqabı", "all": ["ayaqqabı", "çanta", "əlcək"]},
            {"word": "HAT", "correct": "papaq", "all": ["papaq", "şarf", "eynək"]},
            {"word": "DRESS", "correct": "don", "all": ["don", "ətək", "köynək"]},
            {"word": "COAT", "correct": "palto", "all": ["palto", "pencək", "plaş"]},
            {"word": "SOCK", "correct": "corab", "all": ["corab", "əlcək", "şalvar"]},
            {"word": "WATCH", "correct": "saat", "all": ["saat", "eynək", "üzük"]},
            {"word": "GLASSES", "correct": "eynək", "all": ["eynək", "saat", "çanta"]},
            {"word": "BAG", "correct": "çanta", "all": ["çanta", "pulqabı", "kitab"]}
        ],
        "Step 3": [
            {"word": "MARKET", "correct": "bazar", "all": ["bazar", "dükan", "aptek"]},
            {"word": "MONEY", "correct": "pul", "all": ["pul", "kart", "borc"]},
            {"word": "PRICE", "correct": "qiymət", "all": ["qiymət", "endirim", "pul"]},
            {"word": "BUY", "correct": "almaq", "all": ["almaq", "satmaq", "vermək"]},
            {"word": "SELL", "correct": "satmaq", "all": ["satmaq", "almaq", "dəyişmək"]},
            {"word": "CHEAP", "correct": "ucuz", "all": ["ucuz", "bahalı", "pulsuz"]},
            {"word": "EXPENSIVE", "correct": "bahalı", "all": ["bahalı", "ucuz", "adi"]},
            {"word": "FOOD", "correct": "yemək", "all": ["yemək", "içki", "meyvə"]},
            {"word": "MILK", "correct": "süd", "all": ["süd", "su", "şirə"]},
            {"word": "EGG", "correct": "yumurta", "all": ["yumurta", "süd", "yağ"]}
        ],
        "Step 4": [
            {"word": "BIRD", "correct": "quş", "all": ["quş", "balıq", "həşərat"]},
            {"word": "HORSE", "correct": "at", "all": ["at", "eşşək", "dəvə"]},
            {"word": "COW", "correct": "inək", "all": ["inək", "qoyun", "keçi"]},
            {"word": "SHEEP", "correct": "qoyun", "all": ["qoyun", "quzu", "inək"]},
            {"word": "LION", "correct": "aslan", "all": ["aslan", "pələng", "ayı"]},
            {"word": "BEAR", "correct": "ayı", "all": ["ayı", "canavar", "tülkü"]},
            {"word": "WOLF", "correct": "canavar", "all": ["canavar", "it", "tülkü"]},
            {"word": "SNAKE", "correct": "ilan", "all": ["ilan", "qurbağa", "kərtənkələ"]},
            {"word": "RABBIT", "correct": "dovşan", "all": ["dovşan", "siçan", "pişik"]},
            {"word": "MOUSE", "correct": "siçan", "all": ["siçan", "dovşan", "siçovul"]}
        ],
        "Step 5": [
            {"word": "WINTER", "correct": "qış", "all": ["qış", "yay", "payız"]},
            {"word": "SUMMER", "correct": "yay", "all": ["yay", "yaz", "qış"]},
            {"word": "SPRING", "correct": "yaz", "all": ["yaz", "yay", "payız"]},
            {"word": "AUTUMN", "correct": "payız", "all": ["payız", "yaz", "qış"]},
            {"word": "RAIN", "correct": "yağış", "all": ["yağış", "qar", "külək"]},
            {"word": "SNOW", "correct": "qar", "all": ["qar", "yağış", "duman"]},
            {"word": "WIND", "correct": "külək", "all": ["külək", "fırtına", "günəş"]},
            {"word": "HOT", "correct": "isti", "all": ["isti", "soyuq", "ilıq"]},
            {"word": "COLD", "correct": "soyuq", "all": ["soyuq", "isti", "sərin"]},
            {"word": "WEATHER", "correct": "hava", "all": ["hava", "göy", "bulud"]}
        ],
        "Step 6": [
            {"word": "MOUNTAIN", "correct": "dağ", "all": ["dağ", "təpə", "düzənlik"]},
            {"word": "RIVER", "correct": "çay", "all": ["çay", "göl", "dəniz"]},
            {"word": "SEA", "correct": "dəniz", "all": ["dəniz", "okean", "çay"]},
            {"word": "LAKE", "correct": "göl", "all": ["göl", "dəniz", "su bənd"]},
            {"word": "FOREST", "correct": "meşə", "all": ["meşə", "bağ", "çöl"]},
            {"word": "FLOWER", "correct": "gül", "all": ["gül", "ot", "ağac"]},
            {"word": "GRASS", "correct": "ot", "all": ["ot", "gül", "yarpaq"]},
            {"word": "SKY", "correct": "səma", "all": ["səma", "yer", "bulud"]},
            {"word": "MOON", "correct": "ay", "all": ["ay", "günəş", "ulduz"]},
            {"word": "STAR", "correct": "ulduz", "all": ["ulduz", "ay", "planet"]}
        ],
        "Step 7": [
            {"word": "HAPPY", "correct": "xoşbəxt", "all": ["xoşbəxt", "kədərli", "əsəbi"]},
            {"word": "ANGRY", "correct": "əsəbi", "all": ["əsəbi", "sakit", "şən"]},
            {"word": "TIRED", "correct": "yorgun", "all": ["yorgun", "gümrah", "xəstə"]},
            {"word": "HUNGRY", "correct": "acıqmış", "all": ["acıqmış", "tox", "susuz"]},
            {"word": "THIRSTY", "correct": "susuzlamış", "all": ["susuzlamış", "tox", "acıqmış"]},
            {"word": "STRONG", "correct": "güclü", "all": ["güclü", "zəif", "qorxaq"]},
            {"word": "WEAK", "correct": "zəif", "all": ["zəif", "güclü", "cəsur"]},
            {"word": "BRAVE", "correct": "cəsur", "all": ["cəsur", "qorxaq", "zəif"]},
            {"word": "SCARED", "correct": "qorxmuş", "all": ["qorxmuş", "cəsur", "şən"]},
            {"word": "QUIET", "correct": "sakit", "all": ["sakit", "səsli", "əsəbi"]}
        ],
        "Step 8": [
            {"word": "AIRPLANE", "correct": "təyyarə", "all": ["təyyarə", "vertolyot", "gəmi"]},
            {"word": "SHIP", "correct": "gəmi", "all": ["gəmi", "qayıq", "təyyarə"]},
            {"word": "BICYCLE", "correct": "velosiped", "all": ["velosiped", "motosiklet", "maşın"]},
            {"word": "BUS", "correct": "avtobus", "all": ["avtobus", "tramvay", "metro"]},
            {"word": "TRAIN", "correct": "qatar", "all": ["qatar", "metro", "avtobus"]},
            {"word": "TICKET", "correct": "bilet", "all": ["bilet", "pasport", "vizitka"]},
            {"word": "STATION", "correct": "stansiya", "all": ["stansiya", "dayanacaq", "liman"]},
            {"word": "DRIVE", "correct": "sürmək", "all": ["sürmək", "getmək", "qaçmaq"]},
            {"word": "RIDE", "correct": "minmək", "all": ["minmək", "düşmək", "yerimək"]},
            {"word": "TRAVEL", "correct": "səyahət", "all": ["səyahət", "iş", "tətil"]}
        ],
        "Step 9": [
            {"word": "FAST", "correct": "sürətli", "all": ["sürətli", "yavaş", "gec"]},
            {"word": "SLOW", "correct": "yavaş", "all": ["yavaş", "sürətli", "tez"]},
            {"word": "EASY", "correct": "asan", "all": ["asan", "çətin", "mürəkkəb"]},
            {"word": "HARD", "correct": "çətin", "all": ["çətin", "asan", "sadə"]},
            {"word": "RIGHT", "correct": "sağ", "all": ["sağ", "sol", "düz"]},
            {"word": "LEFT", "correct": "sol", "all": ["sol", "sağ", "geridə"]},
            {"word": "UP", "correct": "yuxarı", "all": ["yuxarı", "aşağı", "yan"]},
            {"word": "DOWN", "correct": "aşağı", "all": ["aşağı", "yuxarı", "içəri"]},
            {"word": "CLEAN", "correct": "təmiz", "all": ["təmiz", "çirkli", "köhnə"]},
            {"word": "DIRTY", "correct": "çirkli", "all": ["çirkli", "təmiz", "yeni"]}
        ],
        "Step 10": [
            {"word": "LISTEN", "correct": "dinləmək", "all": ["dinləmək", "danışmaq", "oxumaq"]},
            {"word": "SPEAK", "correct": "danışmaq", "all": ["danışmaq", "eşitmək", "yazmaq"]},
            {"word": "HEAR", "correct": "eşitmək", "all": ["eşitmək", "baxmaq", "toxunmaq"]},
            {"word": "SMELL", "correct": "iyləmək", "all": ["iyləmək", "dadmaq", "görmək"]},
            {"word": "TASTE", "correct": "dadmaq", "all": ["dadmaq", "iyləmək", "yemək"]},
            {"word": "TOUCH", "correct": "toxunmaq", "all": ["toxunmaq", "tutmaq", "itələmək"]},
            {"word": "OPEN", "correct": "açmaq", "all": ["açmaq", "bağlamaq", "yırtmaq"]},
            {"word": "CLOSE", "correct": "bağlamaq", "all": ["bağlamaq", "açmaq", "gizlətmək"]},
            {"word": "WAIT", "correct": "gözləmək", "all": ["gözləmək", "getmək", "gəlmək"]},
            {"word": "STOP", "correct": "dayanmaq", "all": ["dayanmaq", "başlamaq", "davam etmək"]}
        ]
    },"Level 3": {
        "Step 1": [
            {"word": "HEALTH", "correct": "sağlamlıq", "all": ["sağlamlıq", "xəstəlik", "dərman"]},
            {"word": "ADVICE", "correct": "məsləhət", "all": ["məsləhət", "sual", "cavab"]},
            {"word": "BELIEVE", "correct": "inanmaq", "all": ["inanmaq", "şübhələnmək", "görmək"]},
            {"word": "CHANCE", "correct": "şans", "all": ["şans", "təhlükə", "qəza"]},
            {"word": "DANGER", "correct": "təhlükə", "all": ["təhlükə", "təhlükəsizlik", "ehtimal"]},
            {"word": "FAMOUS", "correct": "məşhur", "all": ["məşhur", "adi", "tanınmaz"]},
            {"word": "FORGET", "correct": "unutmaq", "all": ["unutmaq", "xatırlamaq", "bilmək"]},
            {"word": "HISTORY", "correct": "tarix", "all": ["tarix", "gələcək", "elm"]},
            {"word": "ISLAND", "correct": "ada", "all": ["ada", "dağ", "meşə"]},
            {"word": "JOURNEY", "correct": "səyahət", "all": ["səyahət", "iş", "yuxu"]}
        ],
        "Step 2": [
            {"word": "KNOWLEDGE", "correct": "bilik", "all": ["bilik", "güc", "kitab"]},
            {"word": "LAUGH", "correct": "gülmək", "all": ["gülmək", "ağlamaq", "susmaq"]},
            {"word": "MEMORY", "correct": "yaddaş", "all": ["yaddaş", "fikir", "beyin"]},
            {"word": "NATURE", "correct": "təbiət", "all": ["təbiət", "şəhər", "zavod"]},
            {"word": "OPINION", "correct": "rəy", "all": ["rəy", "fakt", "yalan"]},
            {"word": "PERHAPS", "correct": "bəlkə", "all": ["bəlkə", "mütləq", "heç vaxt"]},
            {"word": "REASON", "correct": "səbəb", "all": ["səbəb", "nəticə", "məqsəd"]},
            {"word": "SILENT", "correct": "sakit", "all": ["sakit", "səsli", "qəribə"]},
            {"word": "THOUGHT", "correct": "fikir", "all": ["fikir", "yuxu", "hərəkət"]},
            {"word": "USEFUL", "correct": "faydalı", "all": ["faydalı", "ziyanlı", "boş"]}
        ],
        "Step 3": [
            {"word": "VALLEY", "correct": "vadi", "all": ["vadi", "təpə", "okean"]},
            {"word": "WEALTH", "correct": "sərvət", "all": ["sərvət", "kasıblıq", "borc"]},
            {"word": "ACCIDENT", "correct": "qəza", "all": ["qəza", "uğur", "bayram"]},
            {"word": "BATTLE", "correct": "döyüş", "all": ["döyüş", "sülh", "oyun"]},
            {"word": "CENTURY", "correct": "əsr", "all": ["əsr", "il", "həftə"]},
            {"word": "DECIDE", "correct": "qərar vermək", "all": ["qərar vermək", "fikirləşmək", "soruşmaq"]},
            {"word": "ENERGY", "correct": "enerji", "all": ["enerji", "yorğunluq", "yuxu"]},
            {"word": "FUTURE", "correct": "gələcək", "all": ["gələcək", "keçmiş", "indi"]},
            {"word": "GOVERNMENT", "correct": "hökumət", "all": ["hökumət", "xalq", "ordu"]},
            {"word": "HONEST", "correct": "düzgün", "all": ["düzgün", "yalançı", "oğru"]}
        ],
        "Step 4": [
            {"word": "IMPORTANT", "correct": "vacib", "all": ["vacib", "lazımsız", "kiçik"]},
            {"word": "KINDNESS", "correct": "mehribanlıq", "all": ["mehribanlıq", "kobudluq", "qəzəb"]},
            {"word": "LIBRARY", "correct": "kitabxana", "all": ["kitabxana", "məktəb", "muzey"]},
            {"word": "MESSAGE", "correct": "ismarıc", "all": ["ismarıc", "zəng", "məktub"]},
            {"word": "NEIGHBOR", "correct": "qonşu", "all": ["qonşu", "dost", "düşmən"]},
            {"word": "OBJECT", "correct": "əşya", "all": ["əşya", "insan", "heyvan"]},
            {"word": "PATIENT", "correct": "səbirli", "all": ["səbirli", "tələsik", "əsəbi"]},
            {"word": "QUALITY", "correct": "keyfiyyət", "all": ["keyfiyyət", "say", "qiymət"]},
            {"word": "REPORT", "correct": "hesabat", "all": ["hesabat", "xəbər", "reklam"]},
            {"word": "SERVICE", "correct": "xidmət", "all": ["xidmət", "satış", "istehsal"]}
        ],
        "Step 5": [
            {"word": "TOWEL", "correct": "dəsmal", "all": ["dəsmal", "sabun", "fırça"]},
            {"word": "UMBRELLA", "correct": "çətir", "all": ["çətir", "papaq", "palto"]},
            {"word": "VACATION", "correct": "tətil", "all": ["tətil", "iş", "məktəb"]},
            {"word": "WEATHER", "correct": "hava", "all": ["hava", "torpaq", "od"]},
            {"word": "YOUTH", "correct": "gənclik", "all": ["gənclik", "qocalıq", "uşaqlıq"]},
            {"word": "ABOVE", "correct": "yuxarıda", "all": ["yuxarıda", "aşağıda", "yanında"]},
            {"word": "BEFORE", "correct": "əvvəl", "all": ["əvvəl", "sonra", "indi"]},
            {"word": "CORNER", "correct": "künc", "all": ["künc", "mərkəz", "düz"]},
            {"word": "DURING", "correct": "ərzində", "all": ["ərzində", "əvvəlində", "sonunda"]},
            {"word": "EXCEPT", "correct": "başqa", "all": ["başqa", "birlikdə", "həmçinin"]}
        ],
        "Step 6": [
            {"word": "FEATHER", "correct": "lələk", "all": ["lələk", "yun", "dəri"]},
            {"word": "GARDEN", "correct": "bağça", "all": ["bağça", "tarla", "meşə"]},
            {"word": "HOPE", "correct": "ümid", "all": ["ümid", "qorxu", "kədər"]},
            {"word": "INSIDE", "correct": "içəri", "all": ["içəri", "çöl", "uzaq"]},
            {"word": "JOY", "correct": "sevinc", "all": ["sevinc", "qəm", "hiris"]},
            {"word": "KITCHEN", "correct": "mətbəx", "all": ["mətbəx", "hamam", "zal"]},
            {"word": "LUCKY", "correct": "şanslı", "all": ["şanslı", "bədbəxt", "kasıb"]},
            {"word": "MIRROR", "correct": "güzgü", "all": ["güzgü", "şüşə", "pəncərə"]},
            {"word": "NARROW", "correct": "dar", "all": ["dar", "geniş", "uzun"]},
            {"word": "OUTSIDE", "correct": "çöl", "all": ["çöl", "içəri", "yaxın"]}
        ],
        "Step 7": [
            {"word": "POCKET", "correct": "cib", "all": ["cib", "çanta", "qutu"]},
            {"word": "QUICKLY", "correct": "tez", "all": ["tez", "yavaş", "gec"]},
            {"word": "READY", "correct": "hazır", "all": ["hazır", "məşğul", "boş"]},
            {"word": "SHADOW", "correct": "kölgə", "all": ["kölgə", "işiq", "bulud"]},
            {"word": "TICKET", "correct": "bilet", "all": ["bilet", "pul", "kart"]},
            {"word": "UNUSUAL", "correct": "qeyri-adi", "all": ["qeyri-adi", "adi", "sadə"]},
            {"word": "VILLAGE", "correct": "kənd", "all": ["kənd", "şəhər", "paytaxt"]},
            {"word": "WARNING", "correct": "xəbərdarlıq", "all": ["xəbərdarlıq", "təbrik", "dəvət"]},
            {"word": "ALREADY", "correct": "artıq", "all": ["artıq", "hələ", "heç vaxt"]},
            {"word": "BELOW", "correct": "aşağıda", "all": ["aşağıda", "yuxarıda", "üstündə"]}
        ],
        "Step 8": [
            {"word": "CAREFUL", "correct": "ehtiyatlı", "all": ["ehtiyatlı", "tələsik", "qorxusuz"]},
            {"word": "DIFFERENT", "correct": "fərqli", "all": ["fərqli", "eyni", "oxşar"]},
            {"word": "ENOUGH", "correct": "kifayət", "all": ["kifayət", "az", "çox"]},
            {"word": "FRESH", "correct": "təzə", "all": ["təzə", "köhnə", "çürük"]},
            {"word": "GENTLE", "correct": "nəzakətli", "all": ["nəzakətli", "kobud", "sərt"]},
            {"word": "HUNGRY", "correct": "ac", "all": ["ac", "tox", "susuz"]},
            {"word": "INSTEAD", "correct": "əvəzinə", "all": ["əvəzinə", "birlikdə", "sonra"]},
            {"word": "LOVELY", "correct": "gözəl", "all": ["gözəl", "çirkin", "pis"]},
            {"word": "MIDDLE", "correct": "orta", "all": ["orta", "kənar", "başlanğıc"]},
            {"word": "NOBODY", "correct": "heç kim", "all": ["heç kim", "hər kəs", "bəziləri"]}
        ],
        "Step 9": [
            {"word": "OFTEN", "correct": "tez-tez", "all": ["tez-tez", "hərdən", "heç vaxt"]},
            {"word": "POSSIBLE", "correct": "mümkün", "all": ["mümkün", "qeyri-mümkün", "çətin"]},
            {"word": "QUIETLY", "correct": "sakitcə", "all": ["sakitcə", "bərkdən", "sürətlə"]},
            {"word": "RATHER", "correct": "daha çox", "all": ["daha çox", "az", "heç"]},
            {"word": "SEVERAL", "correct": "bir neçə", "all": ["bir neçə", "çox", "tək"]},
            {"word": "THROUGH", "correct": "vasitəsilə", "all": ["vasitəsilə", "qarşısında", "yanında"]},
            {"word": "USELESS", "correct": "faydasız", "all": ["faydasız", "vacib", "lazımlı"]},
            {"word": "VALUABLE", "correct": "qiymətli", "all": ["qiymətli", "ucuz", "boş"]},
            {"word": "WITHOUT", "correct": "olmadan", "all": ["olmadan", "ilə", "üçün"]},
            {"word": "WHILE", "correct": "ərzində", "all": ["ərzində", "sonra", "əvvəl"]}
        ],
        "Step 10": [
            {"word": "AGAINST", "correct": "əleyhinə", "all": ["əleyhinə", "tərəfində", "ilə"]},
            {"word": "BETWEEN", "correct": "arasında", "all": ["arasında", "üstündə", "altında"]},
            {"word": "COMMON", "correct": "ümumi", "all": ["ümumi", "xüsusi", "fərqli"]},
            {"word": "DISTANCE", "correct": "məsafə", "all": ["məsafə", "yaxınlıq", "hündürlük"]},
            {"word": "EVERYWHERE", "correct": "hər yerdə", "all": ["hər yerdə", "heç yerdə", "orada"]},
            {"word": "FOLLOW", "correct": "izləmək", "all": ["izləmək", "qaçmaq", "durmaq"]},
            {"word": "GENERAL", "correct": "ümumi", "all": ["ümumi", "sirr", "şəxsi"]},
            {"word": "HAPPEN", "correct": "baş vermək", "all": ["baş vermək", "itirmək", "tapmaq"]},
            {"word": "IMPROVE", "correct": "təkmilləşdirmək", "all": ["təkmilləşdirmək", "korlamaq", "saxlamaq"]},
            {"word": "LESSON", "correct": "dərs", "all": ["dərs", "oyun", "istirahət"]}
        ]
    },
    "Level 4": {
        "Step 1": [
            {"word": "ACCOUNT", "correct": "hesab", "all": ["hesab", "şifrə", "ad"]},
            {"word": "ADVERTISE", "correct": "reklam etmək", "all": ["reklam etmək", "satmaq", "almaq"]},
            {"word": "AMOUNT", "correct": "məbləğ", "all": ["məbləğ", "say", "ölçü"]},
            {"word": "APPOINTMENT", "correct": "görüş", "all": ["görüş", "dərs", "tətil"]},
            {"word": "APPROVE", "correct": "təsdiqləmək", "all": ["təsdiqləmək", "imtina etmək", "yoxlamaq"]},
            {"word": "AVAILABLE", "correct": "mövcud", "all": ["mövcud", "məşğul", "bitmiş"]},
            {"word": "AVERAGE", "correct": "orta", "all": ["orta", "yüksək", "alçaq"]},
            {"word": "BALANCE", "correct": "balans", "all": ["balans", "çəki", "fərq"]},
            {"word": "BENEFIT", "correct": "fayda", "all": ["fayda", "ziyan", "borc"]},
            {"word": "BUDGET", "correct": "büdcə", "all": ["büdcə", "pul", "maaş"]}
        ],
        "Step 2": [
            {"word": "CANCEL", "correct": "ləğv etmək", "all": ["ləğv etmək", "başlamaq", "davam etmək"]},
            {"word": "CAPACITY", "correct": "tutum", "all": ["tutum", "güc", "həcm"]},
            {"word": "CELEBRATE", "correct": "qeyd etmək", "all": ["qeyd etmək", "yas tutmaq", "unutmaq"]},
            {"word": "CHALLENGE", "correct": "çətinlik", "all": ["çətinlik", "asanlıq", "oyun"]},
            {"word": "COMFORTABLE", "correct": "rahat", "all": ["rahat", "narahat", "sərt"]},
            {"word": "COMMUNITY", "correct": "icma", "all": ["icma", "ailə", "şəxs"]},
            {"word": "COMPARE", "correct": "müqayisə etmək", "all": ["müqayisə etmək", "ayırmaq", "birləşdirmək"]},
            {"word": "COMPLAIN", "correct": "şikayət etmək", "all": ["şikayət etmək", "tərifləmək", "susmaq"]},
            {"word": "CONFIRM", "correct": "təsdiq etmək", "all": ["təsdiq etmək", "şübhələnmək", "inkar etmək"]},
            {"word": "CONNECT", "correct": "qoşulmaq", "all": ["qoşulmaq", "ayrılmaq", "itirmək"]}
        ],
        "Step 3": [
            {"word": "CONSEQUENCE", "correct": "nəticə", "all": ["nəticə", "səbəb", "başlanğıc"]},
            {"word": "CONSIDER", "correct": "nəzərə almaq", "all": ["nəzərə almaq", "unutmaq", "atmaq"]},
            {"word": "CONSUMER", "correct": "istehlakçı", "all": ["istehlakçı", "satıcı", "sahibkar"]},
            {"word": "CONTACT", "correct": "əlaqə", "all": ["əlaqə", "ayrılıq", "məsafə"]},
            {"word": "CONTINUE", "correct": "davam etmək", "all": ["davam etmək", "dayanmaq", "bitirmək"]},
            {"word": "CONTRIBUTE", "correct": "töhfə vermək", "all": ["töhfə vermək", "almaq", "mane olmaq"]},
            {"word": "CONTROL", "correct": "idarə etmək", "all": ["idarə etmək", "tabe olmaq", "izləmək"]},
            {"word": "CONVINCE", "correct": "inandırmaq", "all": ["inandırmaq", "aldatmaq", "qorxutmaq"]},
            {"word": "CREATE", "correct": "yaratmaq", "all": ["yaratmaq", "dağıtmaq", "tapmaq"]},
            {"word": "CREATIVE", "correct": "yaradıcı", "all": ["yaradıcı", "tənbəl", "adi"]}
        ],
        "Step 4": [
            {"word": "CUSTOMER", "correct": "müştəri", "all": ["müştəri", "müdir", "işçi"]},
            {"word": "DAMAGE", "correct": "zərər", "all": ["zərər", "xeyir", "təmir"]},
            {"word": "DEBATE", "correct": "mübahisə", "all": ["mübahisə", "razılıq", "söhbət"]},
            {"word": "DECISION", "correct": "qərar", "all": ["qərar", "sual", "şübhə"]},
            {"word": "DELIVERY", "correct": "çatdırılma", "all": ["çatdırılma", "sifariş", "satış"]},
            {"word": "DEMAND", "correct": "tələb", "all": ["tələb", "təklif", "xahiş"]},
            {"word": "DEPEND", "correct": "asılı olmaq", "all": ["asılı olmaq", "müstəqil olmaq", "idarə etmək"]},
            {"word": "DESCRIBE", "correct": "təsvir etmək", "all": ["təsvir etmək", "göstərmək", "gizlətmək"]},
            {"word": "DESIGN", "correct": "dizayn", "all": ["dizayn", "şəkil", "yazı"]},
            {"word": "DEVELOP", "correct": "inkişaf etmək", "all": ["inkişaf etmək", "geriləmək", "durmaq"]}
        ],
        "Step 5": [
            {"word": "DEVICE", "correct": "cihaz", "all": ["cihaz", "oyun", "proqram"]},
            {"word": "DIFFICULTY", "correct": "çətinlik", "all": ["çətinlik", "rahatlıq", "şans"]},
            {"word": "DISCOVER", "correct": "kəşf etmək", "all": ["kəşf etmək", "itirmək", "gizlətmək"]},
            {"word": "DISCUSSION", "correct": "müzakirə", "all": ["müzakirə", "dava", "sükut"]},
            {"word": "DISPLAY", "correct": "ekran", "all": ["ekran", "klaviatura", "siçan"]},
            {"word": "DISTANCE", "correct": "məsafə", "all": ["məsafə", "yaxınlıq", "hündürlük"]},
            {"word": "DISTRIBUTE", "correct": "paylamaq", "all": ["paylamaq", "yığmaq", "gizlətmək"]},
            {"word": "DOCUMENT", "correct": "sənəd", "all": ["sənəd", "kitab", "vərəq"]},
            {"word": "DRAMATIC", "correct": "kəskin", "all": ["kəskin", "yumşaq", "adi"]},
            {"word": "EDUCATION", "correct": "təhsil", "all": ["təhsil", "iş", "əyləncə"]}
        ],
        "Step 6": [
            {"word": "EFFECTIVE", "correct": "effektiv", "all": ["effektiv", "faydasız", "zəif"]},
            {"word": "EFFICIENT", "correct": "məhsuldar", "all": ["məhsuldar", "tənbəl", "yavaş"]},
            {"word": "EFFORT", "correct": "səy", "all": ["səy", "istirahət", "oyun"]},
            {"word": "EMPLOYEE", "correct": "işçi", "all": ["işçi", "müdir", "sahibkar"]},
            {"word": "EMPLOYER", "correct": "işəgötürən", "all": ["işəgötürən", "işçi", "tələbə"]},
            {"word": "ENCOURAGE", "correct": "həvəsləndirmək", "all": ["həvəsləndirmək", "qorxutmaq", "dayandırmaq"]},
            {"word": "ENVIRONMENT", "correct": "ətraf mühit", "all": ["ətraf mühit", "ev", "kosmos"]},
            {"word": "EQUIPMENT", "correct": "avadanlıq", "all": ["avadanlıq", "ərzaq", "geyim"]},
            {"word": "ESSENTIAL", "correct": "vacib", "all": ["vacib", "əlavə", "lazımsız"]},
            {"word": "ESTABLISH", "correct": "qurmaq", "all": ["qurmaq", "dağıtmaq", "tapmaq"]}
        ],
        "Step 7": [
            {"word": "ESTIMATE", "correct": "təxmin etmək", "all": ["təxmin etmək", "bilmək", "ölçmək"]},
            {"word": "EVENT", "correct": "hadisə", "all": ["hadisə", "yuxu", "plan"]},
            {"word": "EXAMINE", "correct": "müayinə etmək", "all": ["müayinə etmək", "baxmaq", "atlammaq"]},
            {"word": "EXCELLENT", "correct": "əla", "all": ["əla", "pis", "orta"]},
            {"word": "EXCHANGE", "correct": "mübadilə", "all": ["mübadilə", "satış", "hədiyyə"]},
            {"word": "EXECUTIVE", "correct": "rəhbər", "all": ["rəhbər", "işçi", "təcrübəçi"]},
            {"word": "EXHIBITION", "correct": "sərgi", "all": ["sərgi", "konsert", "teatr"]},
            {"word": "EXPAND", "correct": "genişlənmək", "all": ["genişlənmək", "daralmaq", "bitmək"]},
            {"word": "EXPECT", "correct": "gözləmək", "all": ["gözləmək", "unutmaq", "imtina etmək"]},
            {"word": "EXPENSE", "correct": "xərc", "all": ["xərc", "gəlir", "mənfəət"]}
        ],
        "Step 8": [
            {"word": "EXPERIENCE", "correct": "təcrübə", "all": ["təcrübə", "bilik", "dərs"]},
            {"word": "EXPLAIN", "correct": "izah etmək", "all": ["izah etmək", "soruşmaq", "dinləmək"]},
            {"word": "EXPLORE", "correct": "araşdırmaq", "all": ["araşdırmaq", "bilmək", "gizlətmək"]},
            {"word": "EXPORT", "correct": "ixrac", "all": ["ixrac", "idxal", "satış"]},
            {"word": "EXPRESSION", "correct": "ifadə", "all": ["ifadə", "söz", "sükut"]},
            {"word": "EXTEND", "correct": "uzatmaq", "all": ["uzatmaq", "qısaltmaq", "kəsmək"]},
            {"word": "EXTERNAL", "correct": "xarici", "all": ["xarici", "daxili", "orta"]},
            {"word": "FACILITY", "correct": "obyekt", "all": ["obyekt", "əşya", "insan"]},
            {"word": "FACTORY", "correct": "fabrik", "all": ["fabrik", "ofis", "ev"]},
            {"word": "FAILURE", "correct": "uğursuzluq", "all": ["uğursuzluq", "uğur", "qələbə"]}
        ],
        "Step 9": [
            {"word": "FEATURE", "correct": "özəllik", "all": ["özəllik", "rəng", "ölçü"]},
            {"word": "FEEDBACK", "correct": "rəy", "all": ["rəy", "sual", "cavab"]},
            {"word": "FINANCE", "correct": "maliyyə", "all": ["maliyyə", "pul", "borc"]},
            {"word": "FLEXIBLE", "correct": "çevik", "all": ["çevik", "sərt", "yavaş"]},
            {"word": "FOCUS", "correct": "diqqət yetirmək", "all": ["diqqət yetirmək", "dağıtmaq", "unutmaq"]},
            {"word": "FUNCTION", "correct": "funksiya", "all": ["funksiya", "oyun", "iş"]},
            {"word": "FUND", "correct": "fond", "all": ["fond", "bank", "pul"]},
            {"word": "GENERATE", "correct": "yaratmaq", "all": ["yaratmaq", "silmək", "tapmaq"]},
            {"word": "GLOBAL", "correct": "qlobal", "all": ["qlobal", "yerli", "kiçik"]},
            {"word": "GOAL", "correct": "məqsəd", "all": ["məqsəd", "xəyal", "oyun"]}
        ],
        "Step 10": [
            {"word": "GUARANTEE", "correct": "zəmanət", "all": ["zəmanət", "təhlükə", "şans"]},
            {"word": "GUIDELINE", "correct": "təlimat", "all": ["təlimat", "qanun", "xəbər"]},
            {"word": "HEADQUARTERS", "correct": "mənzil-qərargah", "all": ["mənzil-qərargah", "şöbə", "ofis"]},
            {"word": "IDENTIFY", "correct": "müəyyən etmək", "all": ["müəyyən etmək", "itirmək", "gizlətmək"]},
            {"word": "IMPACT", "correct": "təsir", "all": ["təsir", "nəticə", "səbəb"]},
            {"word": "IMPLEMENT", "correct": "tətbiq etmək", "all": ["tətbiq etmək", "planlaşdırmaq", "dayandırmaq"]},
            {"word": "INCENTIVE", "correct": "həvəsləndirmə", "all": ["həvəsləndirmə", "cəza", "borc"]},
            {"word": "INCOME", "correct": "gəlir", "all": ["gəlir", "xərc", "vergi"]},
            {"word": "INCREASE", "correct": "artırmaq", "all": ["artırmaq", "azaltmaq", "dayandırmaq"]},
            {"word": "INDEPENDENT", "correct": "müstəqil", "all": ["müstəqil", "asılı", "tabe"]}
        ]
    },
    "Level 5": {
        "Step 1": [
            {"word": "ADVENTURE", "correct": "macəra", "all": ["macəra", "təhlükə", "səyahət"]},
            {"word": "ATTENTION", "correct": "diqqət", "all": ["diqqət", "qayğı", "səs"]},
            {"word": "CELEBRATION", "correct": "bayram", "all": ["bayram", "yas", "iclas"]},
            {"word": "DIRECTION", "correct": "istiqamət", "all": ["istiqamət", "məsafə", "yer"]},
            {"word": "EDUCATION", "correct": "təhsil", "all": ["təhsil", "iş", "oyun"]},
            {"word": "FREEDOM", "correct": "azadlıq", "all": ["azadlıq", "həbs", "məcburiyyət"]},
            {"word": "GENERATION", "correct": "nəsil", "all": ["nəsil", "ailə", "insan"]},
            {"word": "IMAGINATION", "correct": "təxəyyül", "all": ["təxəyyül", "yaddaş", "gerçəklik"]},
            {"word": "KNOWLEDGE", "correct": "bilik", "all": ["bilik", "güc", "təcrübə"]},
            {"word": "LOCATION", "correct": "məkan", "all": ["məkan", "zaman", "istiqamət"]}
        ],
        "Step 2": [
            {"word": "OPPORTUNITY", "correct": "imkan", "all": ["imkan", "maneə", "təhlükə"]},
            {"word": "POPULATION", "correct": "əhali", "all": ["əhali", "ölkə", "şəhər"]},
            {"word": "REACTION", "correct": "reaksiya", "all": ["reaksiya", "hərəkət", "söz"]},
            {"word": "SITUATION", "correct": "vəziyyət", "all": ["vəziyyət", "yer", "zaman"]},
            {"word": "TRADITION", "correct": "ənənə", "all": ["ənənə", "qayda", "qanun"]},
            {"word": "VACATION", "correct": "tətil", "all": ["tətil", "iş", "bayram"]},
            {"word": "WONDERFUL", "correct": "möhtəşəm", "all": ["möhtəşəm", "pis", "adi"]},
            {"word": "EXPERIENCE", "correct": "təcrübə", "all": ["təcrübə", "bilik", "dərs"]},
            {"word": "DIFFERENCE", "correct": "fərq", "all": ["fərq", "oxşarlıq", "eynilik"]},
            {"word": "APPEARANCE", "correct": "xarici görkəm", "all": ["xarici görkəm", "xasiyyət", "ad"]}
        ],
        "Step 3": [
            {"word": "CHALLENGE", "correct": "sınaq", "all": ["sınaq", "oyun", "asanlıq"]},
            {"word": "CONFIDENCE", "correct": "inam", "all": ["inam", "şübhə", "qorxu"]},
            {"word": "CREATIVITY", "correct": "yaradıcılıq", "all": ["yaradıcılıq", "tənbəllik", "iş"]},
            {"word": "DECISION", "correct": "qərar", "all": ["qərar", "sual", "fikir"]},
            {"word": "ENVIRONMENT", "correct": "ətraf mühit", "all": ["ətraf mühit", "kosmos", "ev"]},
            {"word": "FAILURE", "correct": "uğursuzluq", "all": ["uğursuzluq", "qələbə", "şans"]},
            {"word": "GOVERNMENT", "correct": "hökumət", "all": ["hökumət", "xalq", "ordu"]},
            {"word": "HAPPINESS", "correct": "xoşbəxtlik", "all": ["xoşbəxtlik", "kədər", "qəzəb"]},
            {"word": "IMPORTANT", "correct": "vacib", "all": ["vacib", "lazımsız", "kiçik"]},
            {"word": "JOURNEY", "correct": "səyahət", "all": ["səyahət", "yuxu", "qaçış"]}
        ],
        "Step 4": [
            {"word": "LEADERSHIP", "correct": "liderlik", "all": ["liderlik", "tabeçilik", "dostluq"]},
            {"word": "MANAGEMENT", "correct": "idarəetmə", "all": ["idarəetmə", "istehsal", "satış"]},
            {"word": "NECESSARY", "correct": "zəruri", "all": ["zəruri", "əlavə", "boş"]},
            {"word": "OBJECTIVE", "correct": "məqsəd", "all": ["məqsəd", "yol", "vasitə"]},
            {"word": "PERFORMANCE", "correct": "çıxış", "all": ["çıxış", "hazırlıq", "məşq"]},
            {"word": "QUALITY", "correct": "keyfiyyət", "all": ["keyfiyyət", "say", "miqdar"]},
            {"word": "RELATIONSHIP", "correct": "münasibət", "all": ["münasibət", "dava", "ayrılıq"]},
            {"word": "STRATEGY", "correct": "strategiya", "all": ["strategiya", "plan", "oyun"]},
            {"word": "TECHNOLOGY", "correct": "texnologiya", "all": ["texnologiya", "təbiət", "incəsənət"]},
            {"word": "UNIVERSITY", "correct": "universitet", "all": ["universitet", "məktəb", "bağça"]}
        ],
        "Step 5": [
            {"word": "VALUABLE", "correct": "qiymətli", "all": ["qiymətli", "ucuz", "lazımsız"]},
            {"word": "WEALTHY", "correct": "zəngin", "all": ["zəngin", "kasıb", "paxıl"]},
            {"word": "ACCURATE", "correct": "dəqiq", "all": ["dəqiq", "səhv", "təxmini"]},
            {"word": "BENEFICIAL", "correct": "faydalı", "all": ["faydalı", "ziyanlı", "boş"]},
            {"word": "COMMUNITY", "correct": "icma", "all": ["icma", "fərd", "düşmən"]},
            {"word": "DISCOVERY", "correct": "kəşf", "all": ["kəşf", "itki", "sirr"]},
            {"word": "ECONOMY", "correct": "iqtisadiyyat", "all": ["iqtisadiyyat", "siyasət", "tarix"]},
            {"word": "FLEXIBLE", "correct": "çevik", "all": ["çevik", "sərt", "ağır"]},
            {"word": "GLOBAL", "correct": "qlobal", "all": ["qlobal", "yerli", "kiçik"]},
            {"word": "HONESTY", "correct": "dürüstlük", "all": ["dürüstlük", "yalan", "oğurluq"]}
        ],
        "Step 6": [
            {"word": "INDEPENDENT", "correct": "müstəqil", "all": ["müstəqil", "asılı", "tabe"]},
            {"word": "JUSTICE", "correct": "ədalət", "all": ["ədalət", "haqsızlıq", "cinayət"]},
            {"word": "LOGICAL", "correct": "məntiqli", "all": ["məntiqli", "mənasız", "gülməli"]},
            {"word": "MOTIVATION", "correct": "motivasiya", "all": ["motivasiya", "tənbəllik", "qorxu"]},
            {"word": "NEGATIVE", "correct": "mənfi", "all": ["mənfi", "müsbət", "neytral"]},
            {"word": "ORIGINAL", "correct": "orijinal", "all": ["orijinal", "saxta", "köhnə"]},
            {"word": "POSITIVE", "correct": "müsbət", "all": ["müsbət", "mənfi", "pis"]},
            {"word": "REASONABLE", "correct": "ağlabatan", "all": ["ağlabatan", "axmaqca", "bahalı"]},
            {"word": "SUCCESSFUL", "correct": "uğurlu", "all": ["uğurlu", "uğursuz", "zəif"]},
            {"word": "TEMPORARY", "correct": "müvəqqəti", "all": ["müvəqqəti", "daimi", "uzun"]}
        ],
        "Step 7": [
            {"word": "URGENT", "correct": "təcili", "all": ["təcili", "yavaş", "vacib deyil"]},
            {"word": "VICTORY", "correct": "qələbə", "all": ["qələbə", "məğlubiyyət", "döyüş"]},
            {"word": "WILLING", "correct": "istəkli", "all": ["istəkli", "məcburi", "tənbəl"]},
            {"word": "ABILITY", "correct": "bacarıq", "all": ["bacarıq", "zəiflik", "iş"]},
            {"word": "BALANCE", "correct": "tarazlıq", "all": ["tarazlıq", "xaos", "çəki"]},
            {"word": "CAPACITY", "correct": "tutum", "all": ["tutum", "ölçü", "hündürlük"]},
            {"word": "DELIVERY", "correct": "çatdırılma", "all": ["çatdırılma", "alış", "satış"]},
            {"word": "EFFICIENT", "correct": "səmərəli", "all": ["səmərəli", "faydasız", "yavaş"]},
            {"word": "FREQUENT", "correct": "tez-tez", "all": ["tez-tez", "nadir", "heç vaxt"]},
            {"word": "GENEROUS", "correct": "səxavətli", "all": ["səxavətli", "paxıl", "kasıb"]}
        ],
        "Step 8": [
            {"word": "HEALTHY", "correct": "sağlam", "all": ["sağlam", "xəstə", "zəif"]},
            {"word": "IMMEDIATE", "correct": "dərhal", "all": ["dərhal", "sonra", "gec"]},
            {"word": "JUDGMENT", "correct": "mühakimə", "all": ["mühakimə", "bağışlama", "sevgi"]},
            {"word": "KINDNESS", "correct": "mehribanlıq", "all": ["mehribanlıq", "kobudluq", "nifrət"]},
            {"word": "LANGUAGE", "correct": "dil", "all": ["dil", "səs", "yazı"]},
            {"word": "MEASURE", "correct": "ölçü", "all": ["ölçü", "çəki", "həcm"]},
            {"word": "NETWORK", "correct": "şəbəkə", "all": ["şəbəkə", "qrup", "tək"]},
            {"word": "OPINION", "correct": "rəy", "all": ["rəy", "fakt", "yalan"]},
            {"word": "PRACTICE", "correct": "təcrübə", "all": ["təcrübə", "nəzəriyyə", "oyun"]},
            {"word": "QUESTION", "correct": "sual", "all": ["sual", "cavab", "söz"]}
        ],
        "Step 9": [
            {"word": "RELIABLE", "correct": "etibarlı", "all": ["etibarlı", "yalançı", "zəif"]},
            {"word": "SENSITIVE", "correct": "həssas", "all": ["həssas", "kobud", "sakit"]},
            {"word": "THOUGHTFUL", "correct": "düşüncəli", "all": ["düşüncəli", "tələsik", "axmaq"]},
            {"word": "UNIQUE", "correct": "unikal", "all": ["unikal", "adi", "eyni"]},
            {"word": "VARIOUS", "correct": "müxtəlif", "all": ["müxtəlif", "eyni", "tək"]},
            {"word": "WARNING", "correct": "xəbərdarlıq", "all": ["xəbərdarlıq", "təbrik", "dəvət"]},
            {"word": "YOUTH", "correct": "gənclik", "all": ["gənclik", "qocalıq", "ushaqliq"]},
            {"word": "ZONE", "correct": "zona", "all": ["zona", "ölkə", "yer"]},
            {"word": "AMAZING", "correct": "heyrətamiz", "all": ["heyrətamiz", "pis", "adi"]},
            {"word": "BELIEVE", "correct": "inanmaq", "all": ["inanmaq", "şübhələnmək", "görmək"]}
        ],
        "Step 10": [
            {"word": "CONVINCE", "correct": "inandırmaq", "all": ["inandırmaq", "aldatmaq", "qorxutmaq"]},
            {"word": "DEVELOP", "correct": "inkişaf etdirmək", "all": ["inkişaf etdirmək", "yıxmaq", "dayandırmaq"]},
            {"word": "EXPLORE", "correct": "kəşf etmək", "all": ["kəşf etmək", "oturmaq", "yatmaq"]},
            {"word": "FOLLOW", "correct": "izləmək", "all": ["izləmək", "qaçmaq", "durmaq"]},
            {"word": "GUARANTEE", "correct": "zəmanət", "all": ["zəmanət", "təhlükə", "itki"]},
            {"word": "HAPPEN", "correct": "baş vermək", "all": ["baş vermək", "itirmək", "tapmaq"]},
            {"word": "IDENTIFY", "correct": "müəyyən etmək", "all": ["müəyyən etmək", "itirmək", "gizlətmək"]},
            {"word": "IMPROVE", "correct": "təkmilləşdirmək", "all": ["təkmilləşdirmək", "korlamaq", "saxlamaq"]},
            {"word": "MAINTAIN", "correct": "qoruyub saxlamaq", "all": ["qoruyub saxlamaq", "dəyişmək", "atmaq"]},
            {"word": "ORGANIZE", "correct": "təşkil etmək", "all": ["təşkil etmək", "dağıtmaq", "qarışdırmaq"]}
        ]
    }
}
    
    
    
    

# --- PROQRAMIN MƏNTİQİ --- (Dəyişməz hissə)
SAVE_FILE = "master_progress.json"

def main(page: ft.Page):
    page.title = "A1 English Master (5 Levels)"
    page.window_width = 400
    page.window_height = 700
    page.theme_mode = "light"
    page.horizontal_alignment = "center"

    def save_data(l, s):
        with open(SAVE_FILE, "w") as f: json.dump({"lv": l, "st": s}, f)

    def load_data():
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    d = json.load(f)
                    return d.get("lv", 1), d.get("st", 1)
            except: return 1, 1
        return 1, 1

    l_start, s_start = load_data()
    state = {"lv": l_start, "st": s_start, "list": [], "idx": 0, "sehvler": []}

    header = ft.Text("", size=18, weight="bold", color="blue")
    sual_txt = ft.Text("", size=45, weight="bold")
    netice_txt = ft.Text("", size=16, weight="bold")
    options = ft.Column(horizontal_alignment="center", spacing=10)

    def start_game():
        lv_key = f"Level {state['lv']}"
        st_key = f"Step {state['st']}"
        
        # Əgər Level/Step yoxdursa Level 1 Step 1-ə qayıt
        if lv_key not in DATA: state["lv"] = 1; lv_key = "Level 1"
        if st_key not in DATA[lv_key]: state["st"] = 1; st_key = "Step 1"

        state["list"] = DATA[lv_key][st_key].copy()
        state["idx"] = 0
        state["sehvler"] = []
        random.shuffle(state["list"])
        header.value = f"{lv_key.upper()} | STEP {state['st']}"
        yenile()

    def cavab_yoxla(e):
        options.disabled = True
        secilen = e.control.data
        duzgun = state["list"][state["idx"]]["correct"]
        
        if secilen == duzgun:
            e.control.bgcolor = "green"
            e.control.content.controls[0].value = f"{secilen} ✅"
            e.control.content.controls[0].color = "white"
        else:
            e.control.bgcolor = "red"
            e.control.content.controls[0].value = f"{secilen} ❌"
            e.control.content.controls[0].color = "white"
            if state["list"][state["idx"]] not in state["sehvler"]:
                state["sehvler"].append(state["list"][state["idx"]])
        
        page.update()
        time.sleep(1)
        options.disabled = False
        
        state["idx"] += 1
        if state["idx"] >= len(state["list"]):
            if state["sehvler"]:
                state["list"] = state["sehvler"].copy()
                state["sehvler"] = []
                state["idx"] = 0
                yenile()
            else:
                finish_step()
        else:
            yenile()

    def finish_step():
        options.controls.clear()
        sual_txt.value = "MÖHTƏŞƏM! 🎉"
        
        # Növbəti addım məntiqi
        if state["st"] < 10 and f"Step {state['st']+1}" in DATA[f"Level {state['lv']}"]:
            btn_txt = "Növbəti Addım"
            def next_action(e):
                state["st"] += 1
                save_data(state["lv"], state["st"])
                start_game()
        else:
            btn_txt = "Yeni Səviyyəyə Keç"
            def next_action(e):
                state["lv"] += 1
                state["st"] = 1
                save_data(state["lv"], state["st"])
                start_game()

        options.controls.append(ft.ElevatedButton(btn_txt, on_click=next_action, width=250, height=60))
        page.update()

    def yenile():
        it = state["list"][state["idx"]]
        sual_txt.value = it["word"]
        netice_txt.value = f"Söz: {state['idx']+1}/{len(state['list'])}"
        
        v = it["all"].copy()
        random.shuffle(v)
        
        options.controls.clear()
        for x in v:
            options.controls.append(
                ft.Container(
                    content=ft.Row([ft.Text(x, size=20, weight="bold")], alignment="center"),
                    bgcolor="#f0f0f0", height=55, width=320, border_radius=12,
                    on_click=cavab_yoxla, data=x
                )
            )
        page.update()

    page.add(
        ft.Column([
            header, ft.Divider(height=10),
            sual_txt, ft.Divider(height=20, color="transparent"),
            options, ft.Divider(height=20, color="transparent"),
            netice_txt
        ], horizontal_alignment="center")
    )
    start_game()

ft.app(target=main)
