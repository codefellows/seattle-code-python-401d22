import Head from 'next/head';
import { replies } from '@/data';
import { useState } from "react";

// New
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import EightBall from '@/components/EightBall';
import QuestionForm from '@/components/QuestionForm';

export default function Home() {
    const [question, setQuestion] = useState('Ask me anything...');
    const [magicReplies, setMagicReplies] = useState("Thinking...");

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
                <QuestionForm questionAskedHandler={questionAskedHandler} />

                {/* Eight Ball */}
                <EightBall question={question} />

                {/* Answer(Table) */}
                <p className="text-xl text-center">{reply}</p>

            </main>

            {/* Footer */}
            <Footer />
        </div>
    );
}
