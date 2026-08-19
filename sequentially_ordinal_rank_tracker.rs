/*
A scenic location is represented by its name and attractiveness score, where name is a unique string among all locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score, the better the location. If the scores of two locations are equal, then the location with the lexicographically smaller name is better.
You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:
Adding scenic locations, one at a time.
Querying the ith best location of all locations already added, where i is the number of times the system has been queried (including the current query).
For example, when the system is queried for the 4th time, it returns the 4th best location of all locations already added.
Note that the test data are generated so that at any time, the number of queries does not exceed the number of locations added to the system.
Implement the SORTracker class:
SORTracker() Initializes the tracker system.
void add(string name, int score) Adds a scenic location with name and score to the system.
string get() Queries and returns the ith best location, where i is the number of times this method has been invoked (including this invocation).
*/
use std::collections::BinaryHeap;
use std::cmp::Ordering;
use std::cell::RefCell;
struct SORTracker {
  state: RefCell<TrackerState>,
}
struct TrackerState {
  left: BinaryHeap<Location>,
  right: BinaryHeap<std::cmp::Reverse<Location>>,
}
#[derive(Eq, PartialEq)]
struct Location {
  score: i32,
  name: String,
}
/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl SORTracker {
  fn new() -> Self {
    SORTracker {
      state: RefCell::new(TrackerState {
        left: BinaryHeap::new(),
        right: BinaryHeap::new(),
      }),
    }
  }
  fn add(&self, name: String, score: i32) {
    let mut state = self.state.borrow_mut();
    let new_loc = Location {
      score, name
    };
    state.left.push(new_loc);
    let excess = state.left.pop().unwrap();
    state.right.push(std::cmp::Reverse(excess));
  }
  fn get(&self) -> String {
    let mut state = self.state.borrow_mut();
    if let Some(std::cmp::Reverse(best_of_right)) = state.right.pop() {
      state.left.push(best_of_right);
    }
    state.left.peek().unwrap().name.clone()
  }
}
impl Ord for Location {
  fn cmp(&self, other: &Self) -> Ordering {
    match other.score.cmp(&self.score) {
      Ordering::Equal => self.name.cmp(&other.name),
      ord => ord,
    }
  }
}
impl PartialOrd for Location {
  fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
    Some(self.cmp(other))
  }
}
/**
 * Your SORTracker object will be instantiated and called as such:
 * let obj = SORTracker::new();
 * obj.add(name, score);
 * let ret_2: String = obj.get();
 */
