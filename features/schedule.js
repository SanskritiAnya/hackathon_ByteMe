// This file contains functions related to managing and displaying the schedule, such as adding, removing, or updating scheduled events.

const schedule = [];

// Function to add a new event to the schedule
export function addEvent(time, description) {
    const event = { time, description };
    schedule.push(event);
}

// Function to remove an event from the schedule by its index
export function removeEvent(index) {
    if (index >= 0 && index < schedule.length) {
        schedule.splice(index, 1);
    }
}

// Function to update an existing event in the schedule
export function updateEvent(index, newTime, newDescription) {
    if (index >= 0 && index < schedule.length) {
        schedule[index] = { time: newTime, description: newDescription };
    }
}

// Function to get the current schedule
export function getSchedule() {
    return schedule;
}

export function getTodaySchedule() {
  return [
    { time: "10:00 AM", activity: "Speech Therapy" },
    { time: "2:00 PM", activity: "Medication Reminder" }
  ];
}