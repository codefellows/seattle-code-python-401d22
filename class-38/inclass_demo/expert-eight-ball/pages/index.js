import Head from "next/head";
import { replies } from "@/data";
import { useState } from "react";

// New
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import EightBall from "@/components/EightBall";
import QuestionForm from "@/components/QuestionForm";

export default function Home() {
    const [question, setQuestion] = useState("Ask me anything...");
    const [magicReplies, setMagicReplies] = useState([]);

    function questionAskedHandler(event) {
        event.preventDefault();
        setQuestion(event.target.question.value);
        const randomReply = replies[Math.floor(Math.random() * replies.length)];

        const questionObj = {
            id: magicReplies.length + 1,
            question: event.target.question.value,
            reply: randomReply,
        };

        setMagicReplies([...magicReplies, questionObj]);
    }

    return (
        <div>
            <Head>
                <title>Expert 8 Ball</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            {/* Header */}
            <Header answerCount={magicReplies.length} />

            <main className="flex flex-col items-center py-4 space-y-8">
                {/* QuestionForm */}
                <QuestionForm questionAskedHandler={questionAskedHandler} />

                {/* Eight Ball */}
                <EightBall question={question} />

                {/* Replies(Table) */}
                {/* Conditional rendering */}
                {magicReplies.length > 0 ? (
                    <table className="w-1/2 mx-auto my-4 border">
                        <thead>
                            <tr>
                                <th className="border border-black">Ids:</th>
                                <th className="border border-black">
                                    Questions:
                                </th>
                                <th className="border border-black">
                                    Replies:
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {magicReplies.map((magicReply, idx) => {
                                return (
                                    <tr key={idx}>
                                        <td className="p-2 border border-black">
                                            {magicReply.id}
                                        </td>
                                        <td className="p-2 border border-black">
                                            {magicReply.question}
                                        </td>
                                        <td className="p-2 border border-black">
                                            {magicReply.reply}
                                        </td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                ) : (
                    <h2>Thinking...</h2>
                )}
            </main>

            {/* Footer */}
            <Footer />
        </div>
    );
}
