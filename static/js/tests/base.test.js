/**
 * @jest-environment jsdom
 */

/* jshint esversion: 8 */
/**
 * @jest-environment jsdom
 */

const {
  profileMenu,
  menu,
  loginSignup,
  dropdown,
  studentSearchInput,
  undoSearchStudent,
  memberSearchInput,
  undoSearchMember,
} = require('../base');

beforeAll(() => {
  let fs = require("fs");
  let fileContents = fs.readFileSync("base.html", "utf-8");
  document.open();
  document.write(fileContents);
  document.close();
});

describe("elements are present", () => {
  test("profileMenu", () => {
    expect(profileMenu).toBeDefined();
  });

  test("menu", () => {
    expect(menu).toBeDefined();
  });

  test("loginSignup", () => {
    expect(loginSignup).toBeDefined();
  });
  test("dropdown", () => {
    expect(dropdown).toBeDefined();
  });
  test("studentSearchInput", () => {
    expect(studentSearchInput).toBeDefined();
  });
  test("undoSearchStudent", () => {
    expect(undoSearchStudent).toBeDefined();
  });
  test("memberSearchInput", () => {
    expect(memberSearchInput).toBeDefined();
  });
  test("undoSearchMember", () => {
    expect(undoSearchMember).toBeDefined();
  });
  test("searchStudent", () => {
    expect(searchStudent).toBeDefined();
  });
  test("searchMembers", () => {
    expect(searchMembers).toBeDefined();
  });
});

describe("check that timeout is set", () => {
  test("messages", () => {
    // get element by id 'messages-notes'
    let messages = document.getElementById('messages-notes');
    expect(messages).toBeDefined();
    // check that after 2500ms, the element is hidden
    setTimeout(() => {
      expect(messages.style.display).toBe('none');
    }, 2500);
  });
});