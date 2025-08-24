export function getChatbotResponse(message) {
  const lower = message.toLowerCase();

  if (lower.includes("anxious") || lower.includes("worried")) {
    return "It’s okay to feel anxious. Try a 4-7-8 breathing exercise: inhale for 4, hold for 7, exhale for 8.";
  }
  if (lower.includes("tired") || lower.includes("exhausted")) {
    return "You deserve rest. Even 10 minutes of quiet can help recharge your mind.";
  }
  if (lower.includes("angry") || lower.includes("frustrated")) {
    return "Anger is valid. Try writing down what triggered it—then tear it up. Release it.";
  }
  if (lower.includes("happy") || lower.includes("grateful")) {
    return "That’s wonderful to hear. Celebrate the small wins—they matter more than you think.";
  }

  return "I'm here for you. Would you like a calming tip or a breathing exercise?";
}