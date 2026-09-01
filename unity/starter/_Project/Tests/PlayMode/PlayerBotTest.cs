using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.TestTools;

/// <summary>PlayMode-тест: бот на NavMeshAgent должен дойти до цели за N секунд.</summary>
public class PlayerBotTest
{
    [UnityTest]
    public IEnumerator Bot_ReachesGoal_WithinBudget()
    {
        var go = GameObject.CreatePrimitive(PrimitiveType.Capsule);
        var agent = go.AddComponent<NavMeshAgent>();
        var goal = new Vector3(10, 0, 10); // сцена с запечённым NavMesh должна быть загружена
        agent.SetDestination(goal);
        float t = 0;
        while (Vector3.Distance(go.transform.position, goal) > 1f && t < 15f) { t += Time.deltaTime; yield return null; }
        Assert.Less(t, 15f, "бот не дошёл до цели за 15 с");
    }
}
