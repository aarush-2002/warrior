"""
WARRIOR TELEGRAM BOT
23 notifications per day — 100% FREE
"""

import asyncio
import random
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Bot

# ╔══════════════════════════════════════════════════════╗
# ║  PASTE YOUR CREDENTIALS BELOW                       ║
# ║  Replace the text between the quotes                 ║
# ╚══════════════════════════════════════════════════════╝

BOT_TOKEN = "8784972383:AAEJQaGUPDv07oFakxgJU8LKhRem6GGKa6g"
CHAT_ID = "5672418858"
# ══════════════════════════════════════════════════════

bot = Bot(token=BOT_TOKEN)


async def send(msg):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="HTML")
        print(f"[{datetime.now().strftime('%H:%M')}] Sent!")
    except Exception as e:
        print(f"Error: {e}")


# === NOTIFICATIONS ===

async def wake_up():
    msgs = [
        "🌅 <b>4:30 AM — WAKE UP WARRIOR!</b>\n\n"
        "The world is sleeping. Winners are waking up.\n"
        "IIT Patna to Google. Let's GO! 🔥\n\n"
        "✅ Drink warm water\n✅ Eat a banana\n✅ Get ready for workout",

        "⏰ <b>4:30 AM — RISE AND MINE!</b> ⛏️\n\n"
        "New day = New block to place.\n"
        "100 days of lock-in! 💪\n\n"
        "🍌 Banana + water → Workout time!",

        "🔥 <b>4:30 AM — ANOTHER DAY ANOTHER BLOCK!</b>\n\n"
        "While others dream, you BUILD.\n"
        "Google isn't hiring sleepers! 🚀\n\n"
        "Get up. Hydrate. Let's crush it!",
    ]
    await send(random.choice(msgs))


async def morning_workout():
    await send(
        "🏋️ <b>5:00 AM — WORKOUT TIME!</b>\n\n"
        "📍 Your Room | Bodyweight\n"
        "⏱️ 1 Hour\n\n"
        "Open Warrior app → Train → Start Timer! 💪\n\n"
        "Your body is your first ML project! 🧠"
    )


async def post_workout():
    await send(
        "🚿 <b>6:00 AM — WORKOUT DONE!</b>\n\n"
        "💪 Great work!\n\n"
        "✅ Shower\n"
        "✅ Milk + Peanut Butter\n"
        "✅ Get ready for study\n"
        "💧 Drink water!"
    )


async def study_1():
    await send(
        "📺 <b>6:30 AM — STUDY SESSION 1!</b>\n\n"
        "⏱️ 2 hours straight\n"
        "📚 Open app → Study → Start Timer\n\n"
        "🔒 No phone. No distractions.\n"
        "Code along with every video! 💻"
    )


async def study_break():
    await send(
        "☕ <b>8:30 AM — BREAK!</b>\n\n"
        "✅ Stretch 2 min\n"
        "✅ Drink water 💧\n"
        "✅ Walk around\n\n"
        "Session 2 at 8:45!"
    )


async def study_2():
    await send(
        "📺 <b>8:45 AM — SESSION 2!</b>\n\n"
        "⏱️ 2 more hours!\n"
        "💡 Start timer in app!\n\n"
        "Every minute = closer to Google! 🚀"
    )


async def study_done():
    await send(
        "🎉 <b>10:45 AM — MORNING STUDY DONE!</b>\n\n"
        "~2 hrs of content absorbed! 🧠\n\n"
        "✅ Save study time in app\n"
        "✅ Head to college\n"
        "💧 Drink water!\n\n"
        "Practice at 5 PM! 💻"
    )


async def lunch():
    await send(
        "🍽️ <b>1:00 PM — LUNCH!</b>\n\n"
        "Mess food:\n"
        "✅ 3 Roti + Extra Dal\n"
        "✅ Sabzi + Salad + Curd\n"
        "✅ NO fried food\n\n"
        "💧 Water before eating\n"
        "🥗 Salad FIRST"
    )


async def practice():
    await send(
        "💻 <b>5:00 PM — PRACTICE TIME!</b>\n\n"
        "⏱️ 2 hours\n"
        "🎯 Code what you learned today\n\n"
        "✅ Open Colab\n"
        "✅ Start timer\n"
        "✅ Push to GitHub\n\n"
        "\"Talk is cheap. Show me the code.\" 🐧"
    )


async def evening_run():
    await send(
        "🏃 <b>7:00 PM — RUN TIME!</b>\n\n"
        "📍 Road | 1 Hour\n\n"
        "Open app → Train → Running Timer → START!\n\n"
        "🎧 Listen to ML podcast!\n"
        "📏 Log distance after run!"
    )


async def dinner():
    await send(
        "🍽️ <b>8:00 PM — DINNER!</b>\n\n"
        "✅ 2 Roti + Dal + Light Sabzi\n"
        "✅ NO rice at night\n"
        "✅ NO heavy food\n"
        "💧 Water\n\n"
        "Light dinner = Better sleep = Better brain! 🧠"
    )


async def revision():
    await send(
        "📝 <b>9:00 PM — REVISION!</b>\n\n"
        "⏱️ 1 hour\n\n"
        "✅ Review notes\n"
        "✅ Push code to GitHub\n"
        "✅ Log weight in app\n"
        "✅ Fill checklist\n"
        "✅ Plan tomorrow"
    )


async def sleep():
    await send(
        "😴 <b>10:00 PM — SLEEP SOON!</b>\n\n"
        "Brain needs rest to learn! 🧠\n\n"
        "✅ No screen after 10:15\n"
        "✅ Warm milk + haldi\n"
        "✅ Set 4:30 AM alarm\n\n"
        "Good night Warrior! Tomorrow again! 🌙"
    )


async def water():
    msgs = [
        "💧 <b>DRINK WATER!</b>\n\nBrain needs hydration for ML! 🧠",
        "💧 <b>HYDRATION CHECK!</b>\n\nLog it in the app! 🫗",
        "💧 <b>WATER TIME!</b>\n\nDehydration = Brain fog. DRINK! 💪",
    ]
    await send(random.choice(msgs))


async def motivation():
    quotes = [
        "💎 \"Diamonds form under pressure.\"",
        "🔥 \"IIT Patna to Google — block by block!\"",
        "💪 \"Every push-up, every line of code adds up.\"",
        "🧠 \"Your brain is a neural network. Train it daily.\"",
        "🚀 \"100 days from now you'll be a different person.\"",
        "⚡ \"1% better daily = 37x better yearly.\"",
        "🎯 \"Google hires consistency. Be that person.\"",
        "⛏️ \"Mine your potential. Craft your future.\"",
        "🏆 \"Champions are made from the desire to never quit.\"",
        "🐉 \"The Ender Dragon of Google awaits you!\"",
    ]
    await send(random.choice(quotes))


async def daily_summary():
    today = datetime.now().strftime("%A, %B %d")
    await send(
        f"📊 <b>DAILY SUMMARY — {today}</b>\n\n"
        "Check your app for stats! 📱\n\n"
        "☐ Morning Workout?\n"
        "☐ Study Session 1?\n"
        "☐ Study Session 2?\n"
        "☐ Practice?\n"
        "☐ Evening Run?\n"
        "☐ Revision + GitHub?\n"
        "☐ 11 glasses water?\n\n"
        "Log everything in the app! ✅"
    )


# === SCHEDULER ===

def setup_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")

    # Wake + Workout
    scheduler.add_job(wake_up, "cron", hour=4, minute=30)
    scheduler.add_job(morning_workout, "cron", hour=5, minute=0)
    scheduler.add_job(post_workout, "cron", hour=6, minute=0)

    # Study
    scheduler.add_job(study_1, "cron", hour=6, minute=30)
    scheduler.add_job(study_break, "cron", hour=8, minute=30)
    scheduler.add_job(study_2, "cron", hour=8, minute=45)
    scheduler.add_job(study_done, "cron", hour=10, minute=45)

    # Meals
    scheduler.add_job(lunch, "cron", hour=13, minute=0)
    scheduler.add_job(dinner, "cron", hour=20, minute=0)

    # Practice + Run
    scheduler.add_job(practice, "cron", hour=17, minute=0)
    scheduler.add_job(evening_run, "cron", hour=19, minute=0)

    # Revision + Sleep
    scheduler.add_job(revision, "cron", hour=21, minute=0)
    scheduler.add_job(sleep, "cron", hour=22, minute=0)

    # Water (every ~1.5 hrs during day)
    for h in [7, 9, 11, 14, 16, 18]:
        scheduler.add_job(water, "cron", hour=h, minute=0)

    # Motivation (3x/day)
    scheduler.add_job(motivation, "cron", hour=8, minute=0)
    scheduler.add_job(motivation, "cron", hour=15, minute=0)
    scheduler.add_job(motivation, "cron", hour=20, minute=30)

    # Daily summary
    scheduler.add_job(daily_summary, "cron", hour=21, minute=30)

    scheduler.start()
    print("")
    print("=" * 45)
    print("  WARRIOR BOT IS RUNNING!")
    print("=" * 45)
    print(f"  Chat ID: {CHAT_ID}")
    print(f"  Timezone: Asia/Kolkata")
    print(f"  Notifications: 23/day")
    print("=" * 45)
    print("")
    print("  SCHEDULE:")
    print("  4:30  Wake up")
    print("  5:00  Workout")
    print("  6:00  Post-workout")
    print("  6:30  Study 1")
    print("  7:00  Water")
    print("  8:00  Motivation")
    print("  8:30  Break")
    print("  8:45  Study 2")
    print("  9:00  Water")
    print("  10:45 Study done")
    print("  11:00 Water")
    print("  13:00 Lunch")
    print("  14:00 Water")
    print("  15:00 Motivation")
    print("  16:00 Water")
    print("  17:00 Practice")
    print("  18:00 Water")
    print("  19:00 Run")
    print("  20:00 Dinner")
    print("  20:30 Motivation")
    print("  21:00 Revision")
    print("  21:30 Summary")
    print("  22:00 Sleep")
    print("")
    print("  Keep this window OPEN!")
    print("  Press Ctrl+C to stop")
    print("")


async def main():
    setup_scheduler()

    # Send test message
    await send(
        "🤖 <b>WARRIOR BOT ACTIVATED!</b> ⛏️🔥\n\n"
        "Notifications scheduled:\n\n"
        "⏰ 4:30 — Wake up\n"
        "🏋️ 5:00 — Workout\n"
        "📺 6:30 — Study 1\n"
        "📺 8:45 — Study 2\n"
        "🍽️ 1:00 — Lunch\n"
        "💻 5:00 — Practice\n"
        "🏃 7:00 — Run\n"
        "📝 9:00 — Revision\n"
        "😴 10:00 — Sleep\n"
        "💧 6x — Water\n"
        "💎 3x — Motivation\n\n"
        "Let's crush 100 days! 💪"
    )

    # Keep running
    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())