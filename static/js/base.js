/* jshint esversion: 11 */
const profileMenu = document.getElementById("dropdown-profile");
const menu = document.querySelectorAll(".dropdown");
const loginSignup = document.getElementById("dropdown-enter");
const dropdown = document.querySelectorAll(".account__options");
const studentSearchInput = document.getElementById('student-search_here');
const undoSearchStudent = document.getElementById("students-search-undo");
const memberSearchInput = document.getElementById('members-search-here');
const undoSearchMember = document.getElementById("members-search-undo");

// On load
document.addEventListener("DOMContentLoaded", function () {
  // Close dropdown when the target is outside of the navbar container
  document.addEventListener("click", (e) => {
    if (profileMenu) {
      if (
        e.target !== dropdown &&
        e.target !== profileMenu &&
        profileMenu.classList.contains("open")
      ) {
        profileMenu.classList.remove("open");
      }
    } else {
      if (
        e.target !== dropdown &&
        e.target !== loginSignup &&
        loginSignup.classList.contains("open")
      ) {
        loginSignup.classList.remove("open");
      }
    }
  });

  // Close open navbar menu
  menu.forEach((m) =>
    m.addEventListener("click", () => {
      m.classList.toggle("open");
    })
  );

  // Function controls messages's display
  setTimeout(function () {
    let messages = document.getElementById('messages-notes');
    if (messages) {
      messages.style.display = "none";
    }
  }, 2500);


  // If student search input is on the page, listen for input
  studentSearchInput?.addEventListener("keyup", searchStudent);
  memberSearchInput?.addEventListener("keyup", searchMembers);
});

// Search for students
const searchStudent = (e) => {
  let students = document.querySelectorAll('.students__student');
  students.forEach(element => {
    element.style.display = "none";
  });
  // Get search input value
  let searchStudentsData = studentSearchInput.value;
  students.forEach(element => {
    if (element.innerText.includes(searchStudentsData)) {
      element.style.display = "block";
    }
  });

  // Show undo search button if there is a search
  undoSearchStudent.style.display = "flex";
  // Hide undo search button if there is no search
  if (searchStudentsData == "") {
    undoSearchStudent.style.display = "none";
  } else {
    // Reset search input
    undoSearchStudent.addEventListener("click", function () {
      // Clear input, hide undo button, and show all students 
      studentSearchInput.value = "";
      undoSearchStudent.style.display = "none";
      searchStudent();
    });
  }
};

// Search for members
const searchMembers = (e) => {
  let members = document.querySelectorAll('.member');
  members.forEach(element => {
    element.style.display = "none";
  });
  // Get search input value
  let searchMembersData = memberSearchInput.value;
  members.forEach(element => {
    if (element.innerText.includes(searchMembersData)) {
      element.style.display = "block";
    }
  });

  // Show undo search button if there is a search
  undoSearchMember.style.display = "flex";
  // Hide undo search button if there is no search
  if (searchMembersData == "") {
    undoSearchMember.style.display = "none";
  } else {
    // Reset search input
    undoSearchMember.addEventListener("click", function () {
      // Clear input, hide undo button, and show all members 
      memberSearchInput.value = "";
      undoSearchMember.style.display = "none";
      searchMembers();
    });
  }
};

if (typeof module !== "undefined") module.exports = {
  profileMenu,
  menu,
  loginSignup,
  dropdown,
  studentSearchInput,
  undoSearchStudent,
  memberSearchInput,
  undoSearchMember,
};