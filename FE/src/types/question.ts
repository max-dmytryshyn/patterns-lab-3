import Answer from "./answer";

interface Question {
  id: number;
  text: string;
  answers: Answer[];
}

export default Question;
