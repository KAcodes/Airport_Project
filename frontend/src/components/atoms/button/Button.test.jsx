import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import "@testing-library/jest-dom";
import Button from "./Button";

test("renders button", () => {
  const testTitle = "test title";
  const mockOnClick = jest.fn();

  render(<Button title={"test title"} onClick={mockOnClick} />);

  const button = screen.getByText(testTitle);

  expect(button).toBeInTheDocument;
  expect(button).toHaveTextContent(testTitle);
});

test("button on click is called", () => {
  const testTitle = "test title";
  const mockOnClick = jest.fn();

  render(<Button title={"test title"} onClick={mockOnClick} />);

  const button = screen.getByText(testTitle);

  userEvent.click(button);

  expect(mockOnClick).toHaveBeenCalled();
  expect(mockOnClick).toHaveBeenCalledTimes(1);
});

test("button has role button", () => {
  const testTitle = "test title";
  const mockOnClick = jest.fn();

  render(<Button title={"test title"} onClick={mockOnClick} />);

  const button = screen.getByText(testTitle);

  expect(button).toHaveAttribute("role", "button");
});

// to have style
