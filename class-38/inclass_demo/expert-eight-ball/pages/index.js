import Head from 'next/head';
import { replies } from '@/data';
import { useState } from "react";

// New
import Header from '@/components/Header';
import Footer from '@/components/Footer';

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
            <Header />

            <main className="flex flex-col items-center py-4 space-y-8">

                {/* QuestionForm */}
                <form className="flex w-1/2 p-2 my-4 bg-gray-200 mx-auto" onSubmit={questionAskedHandler}>
                    <input name="question" className="flex-auto pl-1"/>
                    <button className="px-1 py-1 bg-gray-400 text-gray-50">Ask</button>
                </form>

                {/* Eight Ball */}
                

                {/* Answer(Table) */}
                <p className="text-xl text-center">{reply}</p>

            </main>

            {/* Footer */}
            <Footer />
        </div>
    );
}
