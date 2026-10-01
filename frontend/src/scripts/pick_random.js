// 1. Word pools grouped by prefix type
const wordPools = {
  adjective: [
    "psychedelic",
    "elite",
    "youthful",
    "adventurous",
    "dreary",
    "muddled",
    "hellish",
    "sturdy",
    "pumped",
    "bewildered",
    "alert",
    "mean",
    "kaput",
    "cheerful",
    "agonizing",
    "solid",
    "level",
    "ragged",
    "sassy",
    "high",
    "extra-small",
    "greasy",
    "zonked",
    "sweltering",
    "hurt",
    "heavenly",
    "capable",
    "wretched",
    "shut",
    "actual",
    "responsible",
    "meaty",
    "soggy",
    "rainy",
    "fluttering",
    "skillful",
    "jumpy",
    "offbeat",
    "capricious",
    "substantial",
    "electrical",
    "jobless",
    "ratty",
    "dull",
    "public",
    "complex",
    "salty",
    "actually",
    "tearful",
    "exotic",
  ],
  adverb: [
    ,
    "accidentally",
    "aggressively",
    "awkwardly",
    "blindly",
    "cautiously",
    "confidently",
    "desperately",
    "dramatically",
    "eventually",
    "frantically",
    "immediately",
    "mysteriously",
    "nervously",
    "painfully",
    "quietly",
    "rapidly",
    "randomly",
    "reluctantly",
    "suspiciously",
    "somehow",
    "suddenly",
    "surprisingly",
    "temporarily",
    "thoroughly",
    "unintentionally",
    "violently",
    "wildly",
    "carefully",
    "incorrectly",
    "repeatedly",
    "slowly",
    "technically",
    "unnecessarily",
    "unsuccessfully",
    "voluntarily",
    "wisely",
    "professionally",
    "optimistically",
    "pessimistically",
    "manually",
  ],
  noun: [
    "employee",
    "month",
    "protection",
    "farmer",
    "community",
    "delivery",
    "control",
    "moment",
    "responsibility",
    "chest",
    "performance",
    "vehicle",
    "computer",
    "inflation",
    "virus",
    "obligation",
    "shopping",
    "replacement",
    "driver",
    "director",
    "secretary",
    "efficiency",
    "possession",
    "historian",
    "instruction",
    "flight",
    "guidance",
    "memory",
    "potato",
    "village",
    "region",
    "photo",
    "river",
    "product",
    "hotel",
    "thanks",
    "communication",
    "winner",
    "tennis",
    "foundation",
    "teacher",
    "cancer",
    "tea",
    "article",
    "lake",
    "discussion",
    "food",
    "police",
    "establishment",
    "people",
  ],
  verb: [
    "lower",
    "freeze",
    "lend",
    "handle",
    "divide",
    "release",
    "matter",
    "collect",
    "practise",
    "bury",
    "feed",
    "continue",
    "separate",
    "price",
    "correct",
    "climb",
    "grant",
    "transport",
    "express",
    "excuse",
    "appoint",
    "protect",
    "notice",
    "carve",
    "centre",
    "predict",
    "describe",
    "confront",
    "compensate",
    "shape",
    "expand",
    "register",
    "gaze",
    "purchase",
    "beat",
    "satisfy",
    "clarify",
    "urge",
    "gain",
    "qualify",
    "explain",
    "relate",
    "substitute",
    "present",
    "exhibit",
    "associate",
    "survive",
    "range",
    "love",
    "hit",
  ],
};

// 2. Helper function to extract type and pick a random word
function getRandomWord(idString) {
  const prefixType = idString.replace(/[0-9]/g, "");
  const currentPool = wordPools[prefixType] || ["Something"];
  const randomIndex = Math.floor(Math.random() * currentPool.length);
  return currentPool[randomIndex];
}

// ==========================================
// 3. Named Event Handler Functions
// ==========================================

// Click handler for individual rows
function handleIndividualRandomize() {
  // 'this' refers to the clicked button
  const container = this.closest(".join");
  const targetId = container.querySelector("label").getAttribute("for");
  const targetInput = document.getElementById(targetId);

  targetInput.value = getRandomWord(targetId);
}

// Helper function to cycle through each input inside the "All" loop
function randomizeSingleInput(input) {
  const targetId = input.id;
  if (targetId) {
    input.value = getRandomWord(targetId);
  }
}

// Click handler for the global "Randomize All" button
function handleRandomizeAll() {
  const allInputs = document.querySelectorAll(".join .input");
  allInputs.forEach(randomizeSingleInput);
}

// ==========================================
// 4. Hooking up the Event Listeners
// ==========================================

// Individual button listeners
const individualButtons = document.querySelectorAll(".tooltip .btn");
individualButtons.forEach(function (button) {
  button.addEventListener("click", handleIndividualRandomize);
});

// Global button listener
const randomAllBtn = document.getElementById("randomAllBtn");
if (randomAllBtn) {
  randomAllBtn.addEventListener("click", handleRandomizeAll);
}
