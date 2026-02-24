import streamlit as st

st.set_page_config(page_title="Your Russian Classics Prescription", page_icon="🪆", layout="centered")

# ── Data ──────────────────────────────────────────────────────────────────────

BOOKS = {
    "CP": {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "rx_title": "The Overthinker's Bible",
        "rx": (
            "Dr. Raskolnikov prescribes this book for you. You clearly have a rich inner life — "
            "by which we mean you've been having a full moral debate with yourself since Tuesday. "
            "*Crime and Punishment* was written specifically for people who feel guilty about things "
            "they haven't even done yet. Dostoevsky saw you coming 150 years ago. "
            "Take one chapter before bed, and please try not to confess to anything at standup."
        ),
        "emoji": "🪓",
    },
    "MM": {
        "title": "The Master and Margarita",
        "author": "Mikhail Bulgakov",
        "rx_title": "The Chaos Connoisseur's Companion",
        "rx": (
            "Congratulations — the devil has personally selected this book for you. "
            "You walk into meetings the way Woland walks into Moscow: everyone ends up confused, "
            "slightly enchanted, and wondering what just happened. "
            "*The Master and Margarita* is a love story, a political satire, and scientific proof "
            "that the most interesting people are always a little bit demonic. "
            "Do not read on public transport — you will laugh at inappropriate moments."
        ),
        "emoji": "😈",
    },
    "WP": {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "rx_title": "The Epic for the Chronically Ambitious",
        "rx": (
            "You have been prescribed *War and Peace*. Yes, all 1,225 pages. "
            "You're the kind of person who sees a problem and immediately needs the full historical "
            "context, geopolitical implications, and philosophical underpinning before responding. "
            "Tolstoy respects this. So do we. "
            "Clear your schedule for approximately the rest of the year, make a large pot of tea, "
            "and accept that this is your life now."
        ),
        "emoji": "⚔️",
    },
    "AK": {
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "rx_title": "The Romantic's Spectacular Ruin",
        "rx": (
            "Your heart is both your greatest strength and your most spectacular liability. "
            "*Anna Karenina* was written for people who feel everything at 200% intensity — "
            "love, jealousy, longing, and the desperate need to be truly understood. "
            "Warning: this book will make you want to either fall passionately in love "
            "or dramatically stare out of train windows. Possibly both simultaneously. "
            "Do not operate heavy machinery while reading Part 7."
        ),
        "emoji": "🚂",
    },
    "DS": {
        "title": "Dead Souls",
        "author": "Nikolai Gogol",
        "rx_title": "The Satirist's Sacred Text",
        "rx": (
            "You see through people's nonsense instantly, and — crucially — you find it hilarious. "
            "*Dead Souls* is a road trip through 19th-century Russia with a charming con man, "
            "a cast of gloriously absurd characters, and the darkest comedy you'll ever read. "
            "Gogol was also deeply, profoundly weird, which is probably why you two will get along "
            "perfectly. Side effects include: laughing alone, then feeling vaguely sad, then laughing again."
        ),
        "emoji": "👻",
    },
    "TI": {
        "title": "The Idiot",
        "author": "Fyodor Dostoevsky",
        "rx_title": "The Pure Heart's Paradox",
        "rx": (
            "You are, according to this highly scientific quiz, too good for this world. "
            "*The Idiot* is about a man so genuinely kind and pure-hearted that Russian society "
            "has absolutely no idea what to do with him. Sound familiar? "
            "Dostoevsky asks: can a truly good person survive in a cynical world? "
            "We'll let you find out. Recommended dosage: one cup of tea per chapter, "
            "one deep breath before the ending."
        ),
        "emoji": "🕊️",
    },
    "EO": {
        "title": "Eugene Onegin",
        "author": "Alexander Pushkin",
        "rx_title": "The Aesthete's Tragedy",
        "rx": (
            "You are stylish, a little melancholic, and you have definitely romanticised rejecting "
            "something good before realising it was actually great. "
            "*Eugene Onegin* is a novel written entirely in verse — yes, verse — because regular "
            "prose simply couldn't contain this much brooding beauty. "
            "Pushkin wrote it for people who feel things deeply but express it with detachment. "
            "Very chic. Extremely painful. You'll love it."
        ),
        "emoji": "🥀",
    },
    "FS": {
        "title": "Fathers and Sons",
        "author": "Ivan Turgenev",
        "rx_title": "The Rebel's Field Manual",
        "rx": (
            "You have opinions. Strong ones. Especially about people who don't question enough. "
            "*Fathers and Sons* features Bazarov, Russia's original nihilist, who rejected everything "
            "— love, tradition, authority — right up until reality caught up with him. "
            "It's about the collision between idealism and the messy truth of being human. "
            "You'll either deeply admire Bazarov or recognise him uncomfortably in yourself. "
            "Either way, it will be a whole thing."
        ),
        "emoji": "🔬",
    },
}

QUESTIONS = [
    {
        "q": "🌅 It's 9am Monday. Your Slack has 47 unread messages. You:",
        "options": [
            ("Spiral into an existential crisis about the nature of work and whether any of this truly matters", {"CP": 2, "TI": 1}),
            ("Make a coffee, stare at the screen, and philosophically decide to respond... tomorrow", {"DS": 2, "EO": 1}),
            ("Jump straight in. Chaos is just opportunity wearing a disguise", {"WP": 2, "MM": 1}),
            ("Reply to everyone with warmth and genuine care. You believe in people", {"TI": 2, "AK": 1}),
            ("Suspect the devil himself sent those messages and act accordingly", {"MM": 2, "CP": 1}),
        ],
    },
    {
        "q": "😤 A colleague takes credit for your idea in a meeting. You:",
        "options": [
            ("Spend three days in silent moral anguish debating whether to say something", {"CP": 2, "TI": 1}),
            ("Laugh. Of course they did. This world is a comedy and you have a front row seat", {"DS": 2, "MM": 1}),
            ("Write a strongly-worded email you will never, ever send", {"EO": 2, "AK": 1}),
            ("Forgive them immediately. You genuinely believe in the goodness of people", {"TI": 2, "WP": 1}),
            ("Declare silent war. History will remember who had the idea first", {"WP": 2, "FS": 1}),
        ],
    },
    {
        "q": "🛋️ Your ideal Saturday involves:",
        "options": [
            ("Long, brooding walks while composing dramatic internal monologues", {"CP": 2, "EO": 1}),
            ("Hosting a dinner party that somehow gets completely out of hand", {"MM": 2, "DS": 1}),
            ("A passionate love affair that will probably end badly but feels incredible", {"AK": 2, "EO": 1}),
            ("Reading, improving yourself, and quietly preparing for greatness", {"WP": 2, "FS": 1}),
            ("Doing absolutely nothing and feeling a vague, pleasant guilt about it", {"TI": 2, "CP": 1}),
        ],
    },
    {
        "q": "🧠 Which sentence speaks directly to your soul?",
        "options": [
            ("\"I suffer, therefore I am\"", {"CP": 2, "TI": 1}),
            ("\"Life is absurd, and honestly? Mood.\"", {"MM": 2, "DS": 1}),
            ("\"Love is everything, even if — especially if — it destroys me\"", {"AK": 2, "EO": 1}),
            ("\"I just want everyone to be okay, is that so much to ask\"", {"TI": 2, "WP": 1}),
            ("\"I reject your values and I'm establishing my own\"", {"FS": 2, "MM": 1}),
        ],
    },
    {
        "q": "🌑 How do you take your existential dread?",
        "options": [
            ("Neat. I lean into it. It's my whole personality and I'm fine with that", {"CP": 2, "EO": 1}),
            ("With dark humour, deployed at slightly inappropriate moments", {"MM": 2, "DS": 1}),
            ("I fall in love. That'll fix it", {"AK": 2, "EO": 1}),
            ("I write a 1,200-page novel about Russian society. Catharsis through volume", {"WP": 2, "FS": 1}),
            ("What existential dread? I choose joy. Every single time", {"TI": 2, "CP": 0}),
        ],
    },
]

# ── App ───────────────────────────────────────────────────────────────────────

st.title("🪆 Your Russian Classics Prescription")
st.caption("A highly scientific literary diagnostic. Answer honestly. Dostoevsky is watching.")
st.markdown("---")

if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

total = len(QUESTIONS)

if not st.session_state.submitted:
    i = st.session_state.current_q

    # Progress bar
    st.caption(f"Question {i + 1} of {total}")
    st.progress((i) / total)
    st.markdown("")

    item = QUESTIONS[i]
    st.markdown(f"**{item['q']}**")
    st.markdown("")

    options_text = [opt[0] for opt in item["options"]]
    choice = st.radio(
        label="choice",
        options=options_text,
        index=None,
        label_visibility="collapsed",
        key=f"radio_{i}",
    )

    st.markdown("")
    is_last = i == total - 1
    btn_label = "🔬 Diagnose me" if is_last else "Next →"

    if st.button(btn_label, use_container_width=True):
        if choice is None:
            st.warning("Pick an answer to continue.")
        else:
            st.session_state.answers[i] = choice
            if is_last:
                st.session_state.submitted = True
            else:
                st.session_state.current_q += 1
            st.rerun()

else:
    # Tally scores
    scores = {k: 0 for k in BOOKS}
    for i, item in enumerate(QUESTIONS):
        answer = st.session_state.answers.get(i)
        for opt_text, points in item["options"]:
            if opt_text == answer:
                for book_key, pts in points.items():
                    scores[book_key] += pts

    winner = max(scores, key=lambda k: scores[k])
    book = BOOKS[winner]

    st.progress(1.0)
    st.markdown("")
    st.markdown(f"## {book['emoji']} Diagnosis complete.")
    st.markdown("---")
    st.markdown(f"### Rx: *{book['rx_title']}*")
    st.markdown(f"# 📖 {book['title']}")
    st.caption(f"by {book['author']}")
    st.markdown("")
    st.info(book["rx"])
    st.markdown("")

    if st.button("🔄 Retake the quiz", use_container_width=True):
        st.session_state.answers = {}
        st.session_state.current_q = 0
        st.session_state.submitted = False
        st.rerun()
