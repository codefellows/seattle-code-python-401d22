export default function QuestionForm({ questionAskedHandler }) {
    return (
        <form
            className="flex w-1/2 p-2 my-4 bg-gray-200 mx-auto"
            onSubmit={questionAskedHandler}
        >
            <input name="question" className="flex-auto pl-1" />
            <button className="px-1 py-1 bg-gray-400 text-gray-50">Ask</button>
        </form>
    );
}
