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

// ==========================================
// 2. Pure Helper Functions
// ==========================================

// Extracts the prefix type and picks a random word
function getRandomWord(idString) {
  const prefixType = idString.replace(/[0-9]/g, "");
  const currentPool = wordPools[prefixType] || ["Something"];
  const randomIndex = Math.floor(Math.random() * currentPool.length);
  return currentPool[randomIndex];
}

// Iterates over an input to randomize it
function randomizeSingleInput(input) {
  if (input && input.id) {
    input.value = getRandomWord(input.id);
  }
}

// Iterates over an input to empty its text value
function clearSingleInput(input) {
  if (input) {
    input.value = "";
  }
}

// ==========================================
// 3. Named Event Handler Functions
// ==========================================

// Click handler for individual row buttons (🔀)
function handleIndividualRandomize(event) {
  event.preventDefault();

  const container = this.closest(".join");
  if (!container) return;

  const label = container.querySelector("label");
  if (!label) return;

  const targetId = label.getAttribute("for");
  const targetInput = document.getElementById(targetId);

  if (targetInput) {
    targetInput.value = getRandomWord(targetId);
  }
}

// Click handler for the global "Randomize All" button
function handleRandomizeAll(event) {
  event.preventDefault();

  const allInputs = document.querySelectorAll(".join input");
  if (allInputs.length === 0) {
    console.warn("Randomize All: No inputs found with selector '.join input'");
    return;
  }

  allInputs.forEach(randomizeSingleInput);
}

// Click handler for the global "Clear All" button
function handleClearAll(event) {
  event.preventDefault();

  const allInputs = document.querySelectorAll(".join input");
  if (allInputs.length === 0) {
    console.warn("Clear All: No inputs found with selector '.join input'");
    return;
  }

  allInputs.forEach(clearSingleInput);
}

// ==========================================
// 4. Dom Ready Execution & Event Binding
// ==========================================
document.addEventListener("DOMContentLoaded", function () {
  // Bind all individual row buttons inside your tooltips
  const individualButtons = document.querySelectorAll(".tooltip .btn");
  individualButtons.forEach(function (button) {
    button.addEventListener("click", handleIndividualRandomize);
  });

  // Bind the global "Randomize All" button
  const randomAllBtn = document.getElementById("random-all");
  if (randomAllBtn) {
    randomAllBtn.addEventListener("click", handleRandomizeAll);
  } else {
    console.warn(
      "Randomize All: Element with ID 'random-all' was not found on the page.",
    );
  }

  // Bind the global "Clear All" button
  const clearAllBtn = document.getElementById("clear-all");
  if (clearAllBtn) {
    clearAllBtn.addEventListener("click", handleClearAll);
  } else {
    console.warn(
      "Clear All: Element with ID 'clear-all' was not found on the page.",
    );
  }
});
