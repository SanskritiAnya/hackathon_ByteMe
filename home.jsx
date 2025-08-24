export default function Home() {
  return (
    <main className="min-h-screen bg-pink-100 flex items-center justify-center p-8">
      <div className="w-full max-w-4xl h-96 flex overflow-hidden">
        {/* Left sidebar - darker pink */}
        <div className="w-1/4 bg-pink-300"></div>

        {/* Right main area - lighter pink with watermark text */}
        <div className="flex-1 bg-pink-200 flex items-center justify-center relative">
          <h1 className="text-7xl font-serif text-pink-300/30 select-none tracking-wide">Star Bond</h1>
        </div>
      </div>
    </main>
  )
}
