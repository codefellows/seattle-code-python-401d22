export default function RepliesTable({ magicReplies }) {
    return (
        {
            magicReplies.length > 0 ? (
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
    )
}
