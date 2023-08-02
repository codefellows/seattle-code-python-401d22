import Head from 'next/head';
import { replies } from '@/data';
import { useState } from "react";

export default function Home() {
    const [question, setQuestion] = useState('Ask me anything...');
    const [reply, setReply] = useState("Thinking...");

    function questionAskedHandler(event) {
        event.preventDefault();
        setQuestion(event.target.question.value);
        const randomReply = replies[Math.floor(Math.random() * replies.length)];
        setReply(randomReply);
    }

    return(
        <div>

            <Head>
                <title>Expert 8 Ball</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            {/* Header */}
            <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
                <h1 className="text-4xl">Expert 8 Ball</h1>
            </header>

            <main className="flex flex-col items-center py-4 space-y-8">

                {/* QuestionForm */}
                <form className="flex w-1/2 p-2 my-4 bg-gray-200 mx-auto" onSubmit={questionAskedHandler}>
                    <input name="question" className="flex-auto pl-1"/>
                    <button className="px-1 py-1 bg-gray-400 text-gray-50">Ask</button>
                </form>

                {/* Eight Ball */}
                <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
                    <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                        <p className="text-xl text-center">{question}</p>
                    </div>
                </div>

                {/* Answer(Table) */}
                <p className="text-xl text-center">{reply}</p>

            </main>

            {/* Footer */}
            <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
                <p>Expert Eight Ball &copy;{new Date().getFullYear()}</p>
            </footer>
        </div>
    );
}
