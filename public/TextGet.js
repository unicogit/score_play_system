
async function main() {
const url = new URL(import.meta.url);
const path = url.searchParams.get("robots.txt");
const response = await fetch(path);
const text = await response.text();
}



