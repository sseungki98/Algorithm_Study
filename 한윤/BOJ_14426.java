package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_14426 {
	
	// Trie 자료 구조에 사용되는 Node Class
	static class Node {
		
		Map<Character, Node> childNode = new HashMap<>();
	}
	
	static class Trie {
		
		Node root = new Node(); // 모든 문자 체크는 root 노드부터 시작
		
		// 문자열 삽입 메서드
		public void insert(String str) {
			
			Node node = root;
			int size = str.length();
			
			for (int i = 0; i < size; i++) {
				// 존재하면 해당 노드로 이동, 존재하지 않으면 새로운 노드 생성
				node = node.childNode.computeIfAbsent(str.charAt(i), key -> new Node());
			}			
		}
		
		// 문자열 탐색 메서드
		public boolean search(String str) {
			
			Node node = root;
			int size = str.length();
			
			for (int i = 0; i < str.length(); i++) {
				// 존재하면 해당 노드로 이동, 존재하지 않으면 null을 저장
				node = node.childNode.getOrDefault(str.charAt(i), null);
				
				// 문자가 존재하지 않으면 false를 반환
				if (node == null) {
					return false;
				}
			}
			
			return true; // 반복문을 탈출한 경우 true를 반환
		}
	}
	
	static int N, M; // 집합 S에 포함되어 있는 문자열의 개수, 검사해야 할 문자열의 개수
	static int ans; // 정답 카운트
		
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
				
		Trie trie = new Trie(); // Trie 자료 구조 생성
		
		for (int i = 0; i < N; i++) {
			trie.insert(br.readLine());
		}
		
		for (int i = 0; i < M; i++) {
			String pattern = br.readLine(); // 검사해볼 문자열
			
			// 해당 단어가 접두어로 존재하는 경우, 카운트 증가
			if (trie.search(pattern)) {
				ans++;
			}
		}
		
		System.out.println(ans);
	}
}
